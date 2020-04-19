from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class CreateFoodWindow(QtWidgets.QWidget):
    toManageFood = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        self.foodName = buildTextbox()
        nameLayout = buildLayout('H', [buildLabel("Name"), self.foodName])

        backButton = buildButton("Back", self.back)
        createButton = buildButton("Create", self.create)
        buttonLayout = buildLayout('H', [backButton, createButton])

        layout = buildLayout('V', [buildLabel("Create Food"), nameLayout, buttonLayout])

        self.setLayout(layout)

    def create(self):
        foods = getFoods()
        if self.foodName.text() and self.foodName.text() not in foods:
            insertFood(self.foodName.text())
            self.back()
    
    def back(self):
        self.toManageFood.emit()