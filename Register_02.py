from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class RegisterWindow(QtWidgets.QWidget):
    toLogin = QtCore.pyqtSignal()
    toHome = QtCore.pyqtSignal()

    def __init__(self, user):
        self.user = user

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

        self.employeeType = ""
        adminRadio = buildRadioButton("Admin", self.employee)
        managerRadio = buildRadioButton("Manager", self.employee)
        staffRadio = buildRadioButton("Staff", self.employee)
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
        if self.employeeType == "":
            self.employeeType == None
        if len(self.passTextbox.text()) < 8:
            QtWidgets.QMessageBox.about(self, "Register Error", "Password must be 8 or more characters.")
            return
        if self.userTextbox.text() and self.passTextbox.text() and self.emailTextbox.text() and self.firstTextbox.text() and self.lastTextbox.text() and self.balanceTextbox.text() and self.passTextbox.text() == self.confirmTextbox.text() and insertUser(self.userTextbox.text(), self.passTextbox.text(), self.emailTextbox.text(), self.firstTextbox.text(), self.lastTextbox.text(), self.balanceTextbox.text(), self.employeeType):
            try:
                bal = float(self.balanceTextbox.text())
                if bal >= 0:
                    self.user.username = self.userTextbox.text()
                    self.toHome.emit()
            except ValueError:
                print("Balance is formatted incorrectly")