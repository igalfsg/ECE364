import Steganography
import numpy as np
import scipy
import zlib
import base64
import re
import os.path
import sys
import re
from PySide.QtGui import *
from PySide.QtCore import *
from SteganographyGUI import *
from scipy.misc import *


#takes care of the dropping of a new image
class Dropin(QGraphicsView):
    newpic = Signal(str)
    def __init_(self, title, parent):
        super(Dropin, self).__init__(title,parent)
        self.setAcceptDrops(True)
        self.imgArr = None
        self.name = None

    def dropEvent(self, e):
        if (e.mimeData().text()[-5:-2] == "png"):
            scn = QtGui.QGraphicsScene()
            pixmap = QtGui.QPixmap(e.mimeData().text()[7:-2])
            gfxPixItem = scn.addPixmap(pixmap)
            self.setScene(scn)
            self.fitInView(gfxPixItem,  Qt.KeepAspectRatio)
            self.show()
            self.imgArr = imread(e.mimeData().text()[7:-2])
            self.newpic.emit('yo')
            self.name = e.mimeData().text()[7:-2]

    def dragMoveEvent(self, event):
        event.accept()
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()
    
        
    

class Consumer(QMainWindow, Ui_MainWindow):

    
    def __init__(self, parent=None):
        self.paylod = None
        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.btnClean.clicked.connect(self.cleanpic)
        self.btnExtract.clicked.connect(self.extractpic)
        self.btnSave.clicked.connect(self.file_save)
        self.chkApplyCompression.stateChanged.connect(self.makecompress)
        self.chkOverride.stateChanged.connect(self.overridechk)
        self.viewCarrier1 = Dropin(self.grpCarrier1, self)
        self.viewCarrier1.setGeometry(QtCore.QRect(10, 40, 361, 281))
        self.viewCarrier1.setObjectName("viewCarrier1")
        self.viewCarrier1.newpic.connect(self.newcarrier)
        self.viewCarrier2 = Dropin(self.grpCarrier2, self)
        self.viewCarrier2.setGeometry(QtCore.QRect(10, 40, 361, 281))
        self.viewCarrier2.setObjectName("viewCarrier2")
        self.viewCarrier2.newpic.connect(self.newcarrier2)
        self.viewPayload1 = Dropin(self.grpPayload1, self)
        self.viewPayload1.setGeometry(QtCore.QRect(10, 40, 361, 281))
        self.viewPayload1.setObjectName("viewPayload1")
        self.viewPayload1.newpic.connect(self.newpayload)
        self.slideCompression.valueChanged.connect(self.updatecompress)
        self.carr = None
        self.carr2 = None
        self.pay2 = None
        self.pay = None
        self.compression = -1
        self.carriersize = 0
        self.payloadsize = 0

    #File_save saves a file in the address selected by the user
    def file_save(self):
        pic = self.carr.embedPayload(self.payload)
        self.lblPayloadFound.setText("Loading")
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        imsave(name[0], pic)
        self.lblPayloadFound.setText("")

    #takes care of the steps needed to accept a new carrier for embeding
    def newcarrier(self):
        self.carr = Steganography.Carrier (self.viewCarrier1.imgArr)
        self.carriersize = self.viewCarrier1.imgArr.size
        self.txtCarrierSize.setText(str(int(self.viewCarrier1.imgArr.size / 8)))
        self.chkOverride.setEnabled(True)
        if(self.carr.payloadExists()):
            self.lblPayloadFound.setText(">>>> Payload Found<<<<")
        else:
            self.lblPayloadFound.setText("")
        if ((self.chkOverride.isChecked() or (self.carr.payloadExists() == False)) and (self.payloadsize > 0 and self.payloadsize < self.carriersize)):
            self.btnSave.setEnabled(True)
        else:
            self.btnSave.setEnabled(False)

    #opens a picture checks for a payload and gives the user options
    def newcarrier2(self):
        self.carr2 = Steganography.Carrier (self.viewCarrier2.imgArr)
        scn =QtGui.QGraphicsScene()
        scn.clear()
        self.viewPayload2.setScene(scn)
        self.viewPayload2.show()
        if(self.carr2.payloadExists()):
            self.btnExtract.setEnabled(True)
            self.btnClean.setEnabled(True)
        else:
            self.btnExtract.setEnabled(False)
            self.btnClean.setEnabled(False)

    #extracts the payload from the given carrier
    def extractpic(self):
        extracted = self.carr2.extractPayload()
        imsave('temp.png', extracted.img)
        scn = QtGui.QGraphicsScene()
        pixmap = QtGui.QPixmap('temp.png')
        gfxPixItem = scn.addPixmap(pixmap)
        self.viewPayload2.setScene(scn)
        self.viewPayload2.fitInView(gfxPixItem,  Qt.KeepAspectRatio)
        self.viewPayload2.show()
        self.btnExtract.setEnabled(False)

    #deletes the carrier from the picture
    def cleanpic(self):
        self.btnExtract.setEnabled(False)
        self.btnClean.setEnabled(False)
        tempimg = self.carr2.clean()
        scn =QtGui.QGraphicsScene()
        scn.clear()
        self.viewPayload2.setScene(scn)
        self.viewPayload2.show()
        imsave(self.viewCarrier2.name,tempimg)


    #accepts new paytload for embeding and does the necesary steps to generate the payload xml
    def newpayload(self):
        self.pay_img = self.viewPayload1.imgArr
        self.payload = Steganography.Payload(self.pay_img,self.compression)
        self.payloadsize = len(self.payload.xml)
        self.txtPayloadSize.setText(str(self.payloadsize))
        self.payloadsize *= 8
        if ((self.chkOverride.isChecked() or (self.carr and self.carr.payloadExists() == False)) and (self.payloadsize > 0 and self.payloadsize < self.carriersize)):
            self.btnSave.setEnabled(True)
        else:
            self.btnSave.setEnabled(False)

    #takes care of the compression checkbox status
    def makecompress(self):
        if self.chkApplyCompression.isChecked():
            self.slideCompression.setEnabled(True)
            self.txtCompression.setEnabled(True)
            self.compression = int(self.txtCompression.text())
            self.updatecompress()
        else:
            self.slideCompression.setEnabled(False)
            self.txtCompression.setEnabled(False)
            self.compression = -1
            self.updatecompress()


    #takes care of the compression slider
    def updatecompress(self):
        self.txtCompression.setText(str(self.slideCompression.value()))
        if self.compression > -1:
            self.compression = self.slideCompression.value()
        self.payload = Steganography.Payload(self.pay_img,self.compression)
        self.payloadsize = len(self.payload.xml)
        self.txtPayloadSize.setText(str(self.payloadsize))
        self.payloadsize *= 8
        if ((self.chkOverride.isChecked() or (self.carr and self.carr.payloadExists() == False)) and (self.payloadsize > 0 and self.payloadsize < self.carriersize)):
            self.btnSave.setEnabled(True)
        else:
            self.btnSave.setEnabled(False)

    #maintains the status of the override flag
    def overridechk(self):
        if ((self.chkOverride.isChecked() or (self.carr and self.carr.payloadExists() == False)) and (self.payloadsize > 0 and self.payloadsize < self.carriersize)):
            self.btnSave.setEnabled(True)
        else:
            self.btnSave.setEnabled(False)








   

   



if __name__ == "__main__":
    currentApp = QtGui.QApplication(sys.argv)
    currentForm = Consumer()
    currentForm.show()
    currentApp.exec_()
