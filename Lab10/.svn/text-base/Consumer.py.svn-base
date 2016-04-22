import sys
import re
from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.clearButton.clicked.connect(self.clearb)
        self.saveToTargetButton.clicked.connect(self.guarda)
        self.loadButton.clicked.connect(self.loadData)
        self.firstNameLineEdit.textChanged.connect(self.somethingtyped)
        self.lastNameLineEdit.textChanged.connect(self.somethingtyped)
        self.addressLineEdit.textChanged.connect(self.somethingtyped)
        self.cityLineEdit.textChanged.connect(self.somethingtyped)
        self.stateLineEdit.textChanged.connect(self.somethingtyped)
        self.zipLineEdit.textChanged.connect(self.somethingtyped)
        self.emailLineEdit.textChanged.connect(self.somethingtyped)

    def clearb(self):
        self.firstNameLineEdit.setText("")
        self.lastNameLineEdit.setText("")
        self.addressLineEdit.setText("")
        self.cityLineEdit.setText("")
        self.stateLineEdit.setText("")
        self.zipLineEdit.setText("")
        self.emailLineEdit.setText("")
        self.loadButton.setDisabled(False)
        self.saveToTargetButton.setEnabled(False)

    def somethingtyped(self):
        if(self.firstNameLineEdit.text() == "" and self.lastNameLineEdit.text() == ""
           and self.addressLineEdit.text() == "" and self.cityLineEdit.text() == ""
           and self.stateLineEdit.text() == "" and self.zipLineEdit.text() == "" and
           self.emailLineEdit.text() == ""):
            self.loadButton.setDisabled(False)
            self.saveToTargetButton.setEnabled(False)
        else:
            self.loadButton.setDisabled(True)
            self.saveToTargetButton.setEnabled(True)

    def guarda(self):
        if(self.firstNameLineEdit.text() == ""):
            self.errorInfoLabel.setText("Error: Invalid First Name")
            return
        if(self.lastNameLineEdit.text() == ""):
            self.errorInfoLabel.setText("Error: Invalid Last Name")
            return
        if(self.addressLineEdit.text() == ""):
            self.errorInfoLabel.setText("Error: Invalid Address")
            return
        if(self.cityLineEdit.text() == ""):
            self.errorInfoLabel.setText("Error: Invalid City")
            return
        if(re.match('[0-9]{5}', self.zipLineEdit.text()) == None):
            self.errorInfoLabel.setText("Error: Invalid Zip")
            return
        temp = self.stateLineEdit.text()
        found = 0
        for i in self.states:
            if i ==temp:
                found = 1
                break
        if found == 0:
            self.errorInfoLabel.setText("Error: Invalid State")
            return
        if (re.match("\w+@\w+\.\w+", self.emailLineEdit.text()) == None):
            self.errorInfoLabel.setText("Error: Invalid email")
            return
        self.errorInfoLabel.setText("")
        xmlstuff = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xmlstuff += '<user>\n'
        xmlstuff += '\t<FirstName>' + self.firstNameLineEdit.text() + '</FirstName>\n'
        xmlstuff += '\t<LastName>' + self.lastNameLineEdit.text() + '</LastName>\n'
        xmlstuff += '\t<Address>' + self.addressLineEdit.text() + '</Address>\n'
        xmlstuff += '\t<City>' + self.cityLineEdit.text() + '</City>\n'
        xmlstuff += '\t<State>' + self.stateLineEdit.text() + '</State>\n'
        xmlstuff += '\t<ZIP>' + self.zipLineEdit.text() + '</ZIP>\n'
        xmlstuff += '\t<Email>' + self.emailLineEdit.text() + '</Email>\n'
        xmlstuff += '</user>\n'
        #print(xmlstuff)
        with open('target.xml', 'w') as myFile:
            myFile.write(xmlstuff)


    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        with open (filePath, 'r') as myFile:
            all_lines = myFile.readlines()
            all_lines.remove(all_lines[0])
            all_lines.remove(all_lines[0])
            items = []
            for i in all_lines:
                item = i.split(">")[1].split("<")[0]
                items.append(item)
                #q = re.search('[<]{1}([\w]+)[>]{1}([\w\s]+)[</]{2}([\w]+)[>]{1}', i)
                #print(q)
        self.firstNameLineEdit.setText(items[0])
        self.lastNameLineEdit.setText(items[1])
        self.addressLineEdit.setText(items[2])
        self.cityLineEdit.setText(items[3])
        self.stateLineEdit.setText(items[4])
        self.zipLineEdit.setText(items[5])
        self.emailLineEdit.setText(items[6])

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)




if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
