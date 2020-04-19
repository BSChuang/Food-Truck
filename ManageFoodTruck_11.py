from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class ManageFoodTruckWindow(QtWidgets.QWidget):
    toHome = QtCore.pyqtSignal()
    toManageFoodTruck = QtCore.pyqtSignal()
    toCreateFoodTruck = QtCore.pyqtSignal()
    toUpdateFoodTruck = QtCore.pyqtSignal(str)

    def __init__(self, user):
        self.user = user
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        self.truckNameTextbox = buildTextbox()
        layout1 = buildLayout('H', [buildLabel("Food Truck Name (contain)"), self.truckNameTextbox])

        self.stationNameCombobox = buildComboBox(getStationNames())
        layout2 = buildLayout('H', [buildLabel("Station Name"), self.stationNameCombobox])
        layout3 = buildLayout('H', [layout1, layout2])

        self.staffMin = buildTextbox(True)
        self.staffMax = buildTextbox(True)

        layout4 = buildLayout('H', [buildLabel("Staff Count"), self.staffMin, buildLabel("-"), self.staffMax])

        self.capacityCheckbox = QtWidgets.QCheckBox("Has Remaining Capacity")

        filterButton = buildButton("Filter", self.filter)

        grid = buildGrid(["Food Truck Name", "Station Name", "Remaining Capacity", "Staff(s)", "# Menu Items"], self.formatForGrid(self.user.filtered))

        layout5 = buildLayout('H', [layout4, self.capacityCheckbox, filterButton])

        backButton = buildButton("Back", self.back)
        createButton = buildButton("Create", self.create)
        updateButton = buildButton("Update", self.update)
        deletebutton = buildButton("Delete", self.delete)

        layout6 = buildLayout('H', [backButton, createButton, updateButton, deletebutton])

        layout = buildLayout('V', [layout3, layout5, grid, layout6])

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

    def filter(self):
        try :
            staffMin = None if self.staffMin.text() == '' else int(self.staffMin.text())
            staffMax = None if self.staffMax.text() == '' else int(self.staffMax.text())
            self.user.filtered = manageFoodTruckFilter(self.user.username, self.truckNameTextbox.text(), self.stationNameCombobox.currentText(), staffMin, staffMax, self.capacityCheckbox.isChecked())
            self.toManageFoodTruck.emit()
        except ValueError as e :
            pass
        
        
    def selectFoodTruck(self):
        radio = self.sender()
        if radio.isChecked():
            self.user.selectedTruck = radio.value

    def back(self):
        self.user.selectedTruck = None
        self.user.filtered = []
        self.toHome.emit()

    def create(self):
        self.toCreateFoodTruck.emit()

    def update(self):
        print(self.user.selectedTruck)
        if self.user.selectedTruck != None:
            self.toUpdateFoodTruck.emit(self.user.selectedTruck)

    def delete(self):
        if self.user.selectedTruck != None:
            deleteFoodTruck(self.user.selectedTruck)


        