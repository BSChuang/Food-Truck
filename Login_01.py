from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class LoginWindow(QtWidgets.QWidget):
    toHome = QtCore.pyqtSignal()
    toRegister = QtCore.pyqtSignal()

    def __init__(self, user):
        self.user = user
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Login')

        self.userTextbox = buildTextbox()
        userLayout = buildLayout("H", [buildLabel("Username"), self.userTextbox])

        self.passTextbox = buildTextbox()
        passLayout = buildLayout("H", [buildLabel("Password"), self.passTextbox])

        loginButton = buildButton("Login", self.login)
        registerButton = buildButton("Register", self.register)
        buttonLayout = buildLayout('H', [loginButton, registerButton])

        layout = buildLayout("V", [buildLabel("GT Food Truck"), userLayout, passLayout, buttonLayout])
        
        self.setLayout(layout)

    def login(self):
        username = self.userTextbox.text()
        password = self.passTextbox.text()
        if authenticateUser(username, password):
            self.user.username = username
            self.toHome.emit()

    def register(self):
        self.toRegister.emit()