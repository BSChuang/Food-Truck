from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
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
        if username is '' or password is '':
            QMessageBox.about(self, "Login Error", "Must provide username and password.")
        elif authenticateUser(username, password):
            self.user.username = username
            self.toHome.emit()
        else:
            QMessageBox.about(self, "Login Error", "User not found.")

    def register(self):
        self.toRegister.emit()