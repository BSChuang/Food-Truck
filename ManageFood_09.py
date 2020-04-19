from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *
import operator

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

        grid = buildGrid(["Name", "Menu Count", "Purchase Count"], self.formatForGrid(self.user.filtered), user, self)

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

    def sorting(self): # Sort self.user.filtered by the self.user.sortBy and self.user.sortDir
        if self.user.sortBy == "Name":
            self.user.filtered.sort(key=operator.itemgetter(0))
        elif self.user.sortBy == "Menu Count":
            self.user.filtered.sort(key=operator.itemgetter(1))
        elif self.user.sortBy == "Purchase Count":
            self.user.filtered.sort(key=operator.itemgetter(2))

        if self.user.sortDir == "ASC":
            self.user.filtered.reverse()
        
        self.toManageFood.emit()


    def back(self):
        self.user.filtered = []
        self.toHome.emit()

    def delete(self):
        if self.selectedFood is not None:
            deleteFood(self.selectedFood)
            self.user.filtered = []
            self.toManageFood.emit()

    def create(self):
        self.toCreateFood.emit()

        