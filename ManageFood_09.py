from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class ManageFoodWindow(QtWidgets.QWidget):
    toManageFood = QtCore.pyqtSignal()
    toHome = QtCore.pyqtSignal()
    toCreateFood = QtCore.pyqtSignal()

    def __init__(self, user):
        self.user = user
        self.selectedFood = None
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        self.foodNameCombobox = buildComboBox(getFoods())
        filterButton = buildButton("Filter", self.filter)
        hLayout1 = buildLayout('H', [buildLabel("Name"), self.foodNameCombobox, filterButton])

        if self.user.filtered == []:
            self.user.filtered = manageFoodFilter(None, None, None) # TODO implement sorting

        grid = buildGrid(["Name", "Menu Count", "Purchase Count"], self.formatForGrid(self.user.filtered))

        backButton = buildButton("Back", self.back)
        deleteButton = buildButton("Delete", self.delete)
        createButton = buildButton("Create", self.create)

        buttonLayout = buildLayout('H', [backButton, deleteButton, createButton])

        layout = buildLayout('V', [buildLabel("Manage Food"), hLayout1, buildLabel(""), grid, buttonLayout])

        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            name = buildRadioButton(row[0], self.selectFood)
            menuCount = buildLabel(str(row[1]))
            purchaseCount = buildLabel(str(row[2]))
            newList.append((name, menuCount, purchaseCount))
        return newList

    def selectFood(self):
        radio = self.sender()
        if radio.isChecked():
            self.selectedFood = radio.value
        
    def filter(self):
        self.user.filtered = manageFoodFilter(self.foodNameCombobox.currentText(), None, None) # TODO implement sorting
        self.toManageFood.emit()

    def back(self):
        self.user.filtered = []
        self.toHome.emit()

    def delete(self):
        if self.selectedFood is not None:
            deleteFood(self.selectedFood)
            self.toManageFood.emit()

    def create(self):
        self.toCreateFood.emit()

        