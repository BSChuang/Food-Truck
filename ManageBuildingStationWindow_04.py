from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class ManageBuildingStationWindow(QtWidgets.QWidget):
    toHome = QtCore.pyqtSignal()
    toManageBuildingStation = QtCore.pyqtSignal()

    def __init__(self, user):
        self.user = user
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        self.buildingNameCombobox = buildComboBox(getBuildingNames())
        buildingNameLayout = buildLayout('H', [buildLabel("Building Name"), self.buildingNameCombobox])

        self.buildingTagTextbox = buildTextbox()
        buildingTagLayout = buildLayout('H', [buildLabel("Building Tag (contain)"), self.buildingTagTextbox])

        hLayout1 = buildLayout('H', [buildingNameLayout, buildingTagLayout])

        self.stationNameCombobox = buildComboBox(getStationNames())
        stationNameLayout = buildLayout('H', [buildLabel("Station Name"), self.stationNameCombobox])

        self.capacityMin = buildTextbox()
        self.capacityMax = buildTextbox()
        capacityLayout = buildLayout('H', [buildLabel("Capacity"), self.capacityMin, buildLabel("-"), self.capacityMax])

        hLayout2 = buildLayout('H', [stationNameLayout, capacityLayout])

        filterButton = buildButton("Filter", self.filter)

        grid = buildGrid(["Building", "Tag(s)", "Station", "Capacity", "Food Truck(s)"], self.formatForGrid(user.filtered))

        backButton = buildButton("Back", self.back)
        createBuildingButton = buildButton("Create Building", self.createBuilding)
        updateBuildingButton = buildButton("Update Building", self.updateBuilding)
        deleteBuildingButton = buildButton("Delete Building", self.deleteBuilding)
        hLayout3 = buildLayout('H', [createBuildingButton, updateBuildingButton, deleteBuildingButton])
        
        createStationButton = buildButton("Create Station", self.createStation)
        updateStationButton = buildButton("Update Station", self.updateStation)
        deleteStationButton = buildButton("Delete Station", self.deleteStation)
        hLayout4 = buildLayout('H', [createStationButton, updateStationButton, deleteStationButton])

        layout = buildLayout('V', [buildLabel("Manage Building and Station"), hLayout1, hLayout2, filterButton, grid, hLayout3, hLayout4, backButton])

        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            building = buildRadioButton(row[0], self.selectBuilding)
            tags = buildLabel(listToString(row[1]))
            station = buildLabel(row[2])
            capacity = buildLabel(str(row[3]))
            trucks = buildLabel(listToString(row[4]))
            newList.append((building, tags, station, capacity, trucks))

        return newList

    def createBuilding(self):
        pass
    def updateBuilding(self):
        pass
    def deleteBuilding(self):
        pass
    def createStation(self):
        pass
    def updateStation(self):
        pass
    def deleteStation(self):
        pass

    def selectBuilding(self):
        radio = self.sender()
        if radio.isChecked():
            self.selectedBuilding = radio.value

    def filter(self):
        try:
            capacityMin = int(self.capacityMin.text())
            capacityMax = int(self.capacityMax.text())
            if self.buildingNameCombobox.currentText() and self.buildingTagTextbox.text() and self.stationNameCombobox.currentText() and self.capacityMin.text() and self.capacityMax.text() and capacityMin < capacityMax:
                self.user.filtered = manageBuildingStationFilter(self.buildingNameCombobox.currentText(), self.buildingTagTextbox.text(), self.stationNameCombobox.currentText(), self.capacityMin.text(), self.capacityMax.text())
                self.toManageBuildingStation.emit()
        except ValueError as e:
            pass

    def back(self):
        self.user.filtered = []
        self.toHome.emit()
        