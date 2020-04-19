from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *
from CheckableComboBox import CheckableComboBox

class UpdateFoodTruckWindow(QtWidgets.QWidget):
    toManageFoodTruck = QtCore.pyqtSignal()
    toUpdateFoodTruck = QtCore.pyqtSignal(str, str, list)
    
    def __init__(self, user, name, station, staffList):
        self.user = user
        
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        self.nameTextbox = buildTextbox(False, name)
        nameLayout = buildLayout('H', [buildLabel("Name"), self.nameTextbox])
        
        stations = getStationNames()
        if station != '' : 
            stations[0] = station
        else :
            stations[0] = 'PLACEHOLER' # TODO get current station
        self.stationCombobox = buildComboBox(stations)
        stationLayout = buildLayout('H', [buildLabel("Station"), self.stationCombobox])

        self.staff = CheckableComboBox()
        if staffList == None :
            self.staff.addItems(getStaff(self.user.username))
        else :
            self.staff.addItems(staffList)

        staffLayout = buildLayout('H', [buildLabel("Assigned Staff"), self.staff])

        grid = buildGrid(["Food", "Price"], self.formatForGrid(self.user.menuItems))

        self.foodCombobox = buildComboBox(getFoods())
        self.priceTextbox = buildTextbox()
        addButton = buildButton("+", self.addFood)
        newItemLayout = buildLayout('H', [buildLabel("Food"), self.foodCombobox, buildLabel("Price"), self.priceTextbox, addButton])

        backButton = buildButton("Back", self.back)
        updateButton = buildButton("Update", self.update)
        buttonLayout = buildLayout('H', [backButton, updateButton])

        layout = buildLayout('V', [buildLabel("Update Food Truck"), nameLayout, stationLayout, staffLayout, buildLabel("\n Menu Item"), grid, newItemLayout, buttonLayout])

        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            foodName = buildLabel(row[0])
            price = buildLabel(str(row[1]))
            newList.append((foodName, price))
        return newList

    def addFood(self):
        for i in range(len(self.user.menuItems)):
            if self.user.menuItems[i][0] == self.foodCombobox.currentText():
                return

        if self.priceTextbox.text() == "":
            return
        try:
            price = float(self.priceTextbox.text())
            staffString = self.staff.currentText()
            staffList = staffString.split(',')
            staffList.remove('')
            self.user.menuItems.append((self.foodCombobox.currentText(), price))
            self.toUpdateFoodTruck.emit(self.nameTextbox.text(), self.stationCombobox.currentText(), staffList)
        except ValueError:
            return
    
    def back(self):
        self.user.menuItems = []
        self.toManageFoodTruck.emit()

    def update(self):
        staffString = self.staff.currentText()
        staffList = staffString.split(',')
        for staff in staffList:
            if staff == '':
                staffList.remove('')

        if self.nameTextbox.text() and self.stationCombobox.currentText() and len(staffList) != 0 and len(self.user.menuItems) != 0:
            updateFoodTruck(self.nameTextbox.text(), self.stationCombobox.currentText(), staffList, self.user.menuItems)
            self.back()