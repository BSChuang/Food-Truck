from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *
from CheckableComboBox import CheckableComboBox

class CreateFoodTruckWindow(QtWidgets.QWidget):
    toManageFoodTruck = QtCore.pyqtSignal()
    toCreateFoodTruck = QtCore.pyqtSignal()

    def __init__(self, user):
        self.user = user
        
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        self.nameTextbox = buildTextbox()
        nameLayout = buildLayout('H', [buildLabel("Name"), self.nameTextbox])

        self.stationCombobox = buildComboBox(getStationNames())
        stationLayout = buildLayout('H', [buildLabel("Station"), self.stationCombobox])

        self.staff = CheckableComboBox()
        self.staff.addItems(getStaff("Manager 1"))

        staffLayout = buildLayout('H', [buildLabel("Assigned Staff"), self.staff])

        grid = buildGrid(["Food", "Price", "Remove"], self.formatForGrid(self.user.menuItems))

        self.foodCombobox = buildComboBox(getFoods())
        self.priceTextbox = buildTextbox()
        addButton = buildButton("+", self.addFood)
        newItemLayout = buildLayout('H', [buildLabel("Food"), self.foodCombobox, buildLabel("Price"), self.priceTextbox, addButton])

        backButton = buildButton("Back", self.back)
        createButton = buildButton("Create", self.create)
        buttonLayout = buildLayout('H', [backButton, createButton])

        layout = buildLayout('V', [buildLabel("Create Food Truck"), nameLayout, stationLayout, staffLayout, buildLabel("\n Menu Item"), grid, newItemLayout, buttonLayout])

        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            foodName = buildLabel(row[0])
            price = buildLabel(str(row[1]))
            removeButton = buildButton("-", lambda: self.removeFood(row[0]))
            newList.append((foodName, price, removeButton))
        return newList

    def addFood(self):
        for i in range(len(self.user.menuItems)):
            if self.user.menuItems[i][0] == self.foodCombobox.currentText():
                return

        if self.priceTextbox.text() == "":
            return
        try:
            price = float(self.priceTextbox.text())
            self.user.menuItems.append((self.foodCombobox.currentText(), price))
            self.toCreateFoodTruck.emit()
        except ValueError:
            return

    def removeFood(self,foodName):
        for i in range(len(self.user.menuItems)):
            if self.user.menuItems[i][0] == foodName:
                del self.user.menuItems[i]

        self.toCreateFoodTruck.emit()
    
    def back(self):
        self.user.menuItems = []
        self.toManageFoodTruck.emit()

    def create(self):
        staffString = self.staff.currentText()
        staffList = staffString.split(',')
        for staff in staffList:
            if staff == '':
                staffList.remove('')

        if self.nameTextbox.text() and self.stationCombobox.currentText() and len(staffList) != 0 and len(self.user.menuItems) != 0:
            insertFoodTruck(self.nameTextbox.text(), self.stationCombobox.currentText(), staffList, self.user.menuItems)
            self.back()