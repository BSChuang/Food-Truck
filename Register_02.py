from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class RegisterWindow(QtWidgets.QWidget):
    toLogin = QtCore.pyqtSignal()
    toHome = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Register Window')

        self.userTextbox = buildTextbox()
        userLayout = buildLayout("H", [buildLabel("Username"), self.userTextbox])
        self.emailTextbox = buildTextbox()
        emailLayout = buildLayout("H", [buildLabel("Email"), self.emailTextbox])
        hLayout1 = buildLayout("H", [userLayout, emailLayout])

        self.firstTextbox = buildTextbox()
        firstLayout = buildLayout("H", [buildLabel("First Name"), self.firstTextbox])
        self.lastTextbox = buildTextbox()
        lastLayout = buildLayout("H", [buildLabel("Last Name"), self.lastTextbox])
        hLayout2 = buildLayout("H", [firstLayout, lastLayout])

        self.passTextbox = buildTextbox()
        passLayout = buildLayout("H", [buildLabel("Password"), self.passTextbox])
        self.confirmTextbox = buildTextbox()
        confirmLayout = buildLayout("H", [buildLabel("Confirm Password"), self.confirmTextbox])
        hLayout3 = buildLayout("H", [passLayout, confirmLayout])

        self.balanceTextbox = buildTextbox()
        balanceLayout = buildLayout("H", [buildLabel("Balance"), self.balanceTextbox])
        adminRadio = buildRadioButton("admin", self.employee, True)
        managerRadio = buildRadioButton("manager", self.employee)
        staffRadio = buildRadioButton("staff", self.employee)
        self.employeeType = "admin"
        hLayout4 = buildLayout('H', [balanceLayout, adminRadio, managerRadio, staffRadio])

        backButton = buildButton("Back", self.back)
        registerButton = buildButton("Register", self.register)
        hLayout5 = buildLayout('H', [backButton, registerButton])

        layout = buildLayout("V", [buildLabel("Register"), hLayout1, hLayout2, hLayout3, hLayout4, hLayout5])
        self.setLayout(layout)

    def employee(self):
        radio = self.sender()
        if radio.isChecked():
            self.employeeType = radio.value

    def back(self):
        self.toLogin.emit()

    def register(self): # TODO: Add new user to database ------------------------------------------------------------------------------------------------------------
        if self.passTextbox.text() == self.confirmTextbox.text() and insertUser(self.userTextbox.text(), self.passTextbox.text(), self.emailTextbox.text(), self.firstTextbox.text(), self.lastTextbox.text(), self.balanceTextbox.text(), self.employeeType):
            self.toHome.emit()