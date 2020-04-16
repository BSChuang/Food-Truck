from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class CurrentInformation(QtWidgets.QWidget):
    toHome = QtCore.pyqtSignal()
    toOrder = QtCore.pyqtSignal()

    def __init__(self, username):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("Current Information")

        station, building, tags, description, balance = getCurrentInformation(username)

        hLayout1 = buildLayout('H', [buildLabel("Station: "), buildLabel(station)])
        hLayout2 = buildLayout('H', [buildLabel("Building: "), buildLabel(building)])
        hLayout3 = buildLayout('H', [buildLabel("Building Tags: "), buildLabel(listToString(tags))])
        hLayout4 = buildLayout('H', [buildLabel("Building Description: "), buildLabel(description)])
        hLayout5 = buildLayout('H', [buildLabel("Balance: "), buildLabel(str(balance))])

        trucks = getTrucksAtStation(station)
        trucks = self.formatForGrid(trucks)

        grid = buildGrid(["Food Truck", "Manager", "Food(s)"], trucks)

        backButton = buildButton("Back", self.back)
        orderButton = buildButton("Order", self.order)
        buttonLayout = buildLayout("H", [backButton, orderButton])

        totalLayout = buildLayout("V", [buildLabel("Current Information"), hLayout1, hLayout2, hLayout3, hLayout4, hLayout5, grid, buttonLayout])
        self.setLayout(totalLayout)

    def formatForGrid(self, trucks):
        newList = []
        for truck in trucks:
            radio = buildRadioButton(truck[0], self.selectTruck)
            manager = buildLabel(truck[1])
            foods = buildLabel(listToString(truck[2]))
            newList.append((radio, manager, foods))
        return newList
            

        
    def selectTruck(self):
        radio = self.sender()
        if radio.isChecked():
            self.selectedTruck = radio.value

    def back(self):
        self.toHome.emit()
    
    def order(self):
        self.toOrder.emit()