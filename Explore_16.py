from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class ExploreWindow(QtWidgets.QWidget):
    toHome = QtCore.pyqtSignal()
    toExplore = QtCore.pyqtSignal()

    def __init__(self, user):
        self.user = user
        self.username = user.username
        
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        buildingNameList = getBuildingNames()
        self.buildingNameComboBox = buildComboBox(buildingNameList)
        buildingNameLayout = buildLayout('H', [buildLabel("Building Name"), self.buildingNameComboBox])

        stationNameList = getStationNames()
        self.stationNameComboBox = buildComboBox(stationNameList)
        stationNameLayout = buildLayout('H', [buildLabel("Station Name"), self.stationNameComboBox])

        hLayout1 = buildLayout('H', [buildingNameLayout, stationNameLayout])

        self.buildingTagTextbox = buildTextbox()
        buildingTagLayout = buildLayout('H', [buildLabel("Building Tag (contain)"), self.buildingTagTextbox])

        self.foodTruckNameTextbox = buildTextbox()
        foodTruckNameLayout = buildLayout('H', [buildLabel("Food Truck Name (contain)"), self.foodTruckNameTextbox])

        hLayout2 = buildLayout('H', [buildingTagLayout, foodTruckNameLayout])

        self.foodTextbox = buildTextbox()
        foodLayout = buildLayout('H', [buildLabel("Food (contain)"), self.foodTextbox])

        filterButton = buildButton("Filter", self.filter)

        gridLayout = buildGrid(["Station", "Building", "Food Truck(s)", "Food(s)"], self.formatForGrid(user.filtered))

        backButton = buildButton("Back", self.back)
        selectButton = buildButton("Select As Current Location", self.selectAsLocation)
        buttonsLayout = buildLayout('H', [backButton, selectButton])


        layout = buildLayout('V', [buildLabel("Explore"), hLayout1, hLayout2, foodLayout, filterButton, gridLayout, buttonsLayout])

        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            station = buildRadioButton(row[0], self.selectStation)
            building = buildLabel(row[1])
            trucks = buildLabel(listToString(row[2]))
            foods = buildLabel(listToString(row[3]))
            newList.append((station, building, trucks, foods))
        return newList

    def selectStation(self):
        radio = self.sender()
        if radio.isChecked():
            self.selectedStation = radio.value

    def filter(self):
        self.user.filtered = exploreFilter(self.buildingNameComboBox.currentText(), self.stationNameComboBox.currentText(), self.buildingTagTextbox.text(), self.foodTruckNameTextbox.text(), self.foodTextbox.text())
        self.toExplore.emit()

    def back(self):
        self.user.filtered = []
        self.toHome.emit()
    def selectAsLocation(self):
        if self.selectedStation:
            setUserStation(self.username, self.selectedStation)
            self.back()