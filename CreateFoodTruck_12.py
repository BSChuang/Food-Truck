from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *
from CheckableComboBox import CheckableComboBox

class CreateFoodTruckWindow(QtWidgets.QWidget):
    toManageFoodTruck = QtCore.pyqtSignal()

    def __init__(self, user):
        self.user = user
        
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        self.nameTextbox = buildTextbox()
        nameLayout = buildLayout('H', [buildLabel("Name"), self.nameTextbox])

        self.stationCombobox = buildComboBox(getStationNames())
        stationLayout = buildLayout('H', [buildLabel("Station"), self.stationCombobox])

        self.listWidget = CheckableComboBox()
        staff = getStaff("Manager 1")
        self.listWidget.addItems(staff)

        staffLayout = buildLayout('H', [buildLabel("Assigned Staff"), self.listWidget])

        grid = buildGrid(["Food", "Price"], )

        backButton = buildButton("Back", self.back)
        createButton = buildButton("Create", self.create)
        buttonLayout = buildLayout('H', [backButton, createButton])

        layout = buildLayout('V', [buildLabel("Create Food Truck"), nameLayout, stationLayout, staffLayout, buttonLayout])

        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            truckName = buildRadioButton(row[0], self.selectFoodTruck)
            stationName = buildLabel(row[1])
            capacity = buildLabel(str(row[2]))
            staff = buildLabel(str(row[3]))
            menuItem = buildLabel(str(row[4]))
            newList.append((truckName, stationName, capacity, staff, menuItem))
        return newList

    
    def back(self):
        self.toManageFoodTruck.emit()
