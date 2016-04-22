# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *
import re
class CalculatorConsumer(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)
        self.resultado = 0
        self.temp = 0
        self.punto = 0
        self.operador = 0
        self.justfinished = 0
        self.commas = 1
        self.btn9.clicked.connect(self.number_get)
        self.btn8.clicked.connect(self.number_get)
        self.btn7.clicked.connect(self.number_get)
        self.btn6.clicked.connect(self.number_get)
        self.btn5.clicked.connect(self.number_get)
        self.btn4.clicked.connect(self.number_get)
        self.btn3.clicked.connect(self.number_get)
        self.btn2.clicked.connect(self.number_get)
        self.btn1.clicked.connect(self.number_get)
        self.btn0.clicked.connect(self.number_get)
        self.btnClear.clicked.connect(self.limpia)
        self.cboDecimal.activated.connect(self.decimal_get)
        self.btnEqual.clicked.connect(self.igual)
        self.btnDot.clicked.connect(self.dot_get)
        self.btnDivide.clicked.connect(self.get_div)
        self.btnMinus.clicked.connect(self.get_sub)
        self.btnMultiply.clicked.connect(self.get_mul)
        self.btnPlus.clicked.connect(self.get_add)
        self.chkSeparator.stateChanged.connect(self.iscomas)
        self.ndecimal = int(self.cboDecimal.currentText())

    def iscomas(self):
        self.commas = self.chkSeparator.isChecked()
        if not self.commas:
            temporal = self.txtDisplay.text()
            i = re.sub(",","", temporal)
            print(i)
            self.txtDisplay.setText(i)
        else:
            temporal = float(self.txtDisplay.text())
            self.txtDisplay.setText(self.show_num(temporal))

    def decimal_get(self):
        self.ndecimal = int(self.cboDecimal.currentText())


    def number_get(self):
        if (self.temp != 0):
            if(self.punto == 0): #no period yet
                self.temp *= 10
                self.temp += int(self.sender().text())
            else:
                placeh = float(self.sender().text())
                placeh /= (10 ** self.punto)
                self.temp = round(placeh + self.temp, self.punto)
                self.punto += 1
        else:
            if(self.punto == 0):
                self.temp += int(self.sender().text())
            else:
                placeh = float(self.sender().text())
                placeh /= (10)

                self.temp = round(placeh + self.temp, self.punto)
                self.punto += 1
        #update the textbox
        self.txtDisplay.setText(self.show_num(self.temp))
        #self.txtDisplay.setText(str(self.temp))
        self.justfinished = 0



    def show_num(self, num):
        if(self.commas):
            pla = str(int(num) )
            la =""
            x = len(pla) / 3
            if (len(pla) % 3) != 0:
                x +=1
            for i in range(int(x)):
                la = "," + pla[-3:] + la
                pla = pla[:-3]
            la = la[1:]
            print(la)
            if type(num)==float:
                temporal = round(num - int(num), self.ndecimal)
                strtemp = str(temporal)
                la +=  strtemp[1:]
            return la
        else:
            return str(num)


    def dot_get(self):
        if (self.punto == 0):
            self.punto = 1
            self.txtDisplay.setText(self.show_num(self.temp) + '.')
            #self.txtDisplay.setText(str(self.temp) + '.')
        else:
            self.txtDisplay.setText("you can't have multiple decimals #math101")
        self.justfinished = 0


    def get_add(self):
        self.operador = 1
        if(self.justfinished == 0):
            self.resultado = self.temp
        else:
            self.justfinished = 0
        self.temp = 0
        self.punto = 0

    def get_sub(self):
        self.operador = 2
        if(self.justfinished == 0):
            self.resultado = self.temp
        else:
            self.justfinished = 0
        self.temp = 0
        self.punto = 0

    def get_mul(self):
        self.operador = 3
        if(self.justfinished == 0):
            self.resultado = self.temp
        else:
            self.justfinished = 0
        self.temp = 0
        self.punto = 0

    def get_div(self):
        self.operador = 4
        if(self.justfinished == 0):
            self.resultado = self.temp
        else:
            self.justfinished = 0
        self.temp = 0
        self.punto = 0

    def igual(self):
        if(self.operador == 0):
            self.resultado = self.temp
        elif(self.operador == 1): #addition
            self.resultado += self.temp
        elif(self.operador == 2): #substraction
            self.resultado -= self.temp
        elif(self.operador == 3): #multiplication
            self.resultado *= self.temp
        elif(self.operador == 4):#division
            self.resultado = float(self.resultado) / float(self.temp)
        self.resultado = round(self.resultado, self.ndecimal)
        if(self.ndecimal == 0):
            self.resultado = int(self.resultado)
        self.temp = 0
        self.punto = 0
        self.operador = 0
        self.justfinished = 1
        self.txtDisplay.setText(self.show_num(self.resultado))

    def limpia(self):
        self.resultado = 0
        self.temp = 0
        self.punto = 0
        self.operador = 0
        self.justfinished = 0
        self.txtDisplay.setText("0.")




currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()
currentForm.show()
currentApp.exec_()