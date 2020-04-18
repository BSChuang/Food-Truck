from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class ManageBuildingStationWindow(QtWidgets.QWidget):
    toHome = QtCore.pyqtSignal()
    toManageBuildingStation = QtCore.pyqtSignal()
    toCreateBuilding = QtCore.pyqtSignal()
    toUpdateBuilding = QtCore.pyqtSignal(str)
    toCreateStation = QtCore.pyqtSignal()
    toUpdateStation = QtCore.pyqtSignal()

    def __init__(self, user):
        self.user = user
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')
        self.selectedBuilding = None
        
        self.buildingNameCombobox = buildComboBox(getBuildingNames()) # you're probably wondering why I added this blank first
        # well the building name field can be left blank to see all buildings
        buildingNameLayout = buildLayout('H', [buildLabel("Building Name"), self.buildingNameCombobox])

        self.buildingTagTextbox = buildTextbox()
        buildingTagLayout = buildLayout('H', [buildLabel("Building Tag (contain)"), self.buildingTagTextbox])

        hLayout1 = buildLayout('H', [buildingNameLayout, buildingTagLayout])

        stationNames = getStationNames() 
        self.stationNameCombobox = buildComboBox(getStationNames())# you're probably wondering why I added this blank first
        # well the station name field can be left blank to not apply the station filter
        stationNameLayout = buildLayout('H', [buildLabel("Station Name"), self.stationNameCombobox])

        self.capacityMin = buildTextbox(True)
        self.capacityMax = buildTextbox(True)
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
        self.toCreateBuilding.emit()
    def updateBuilding(self):
        #only go to update building if theres one selected
        if not(self.selectedBuilding == None) : 
            self.toUpdateBuilding.emit(self.selectedBuilding)
    def deleteBuilding(self):
        removeBuilding(self.selectedBuilding)
        self.filter()
    def createStation(self):
        self.toCreateStation.emit()
    def updateStation(self):
        self.toUpdateStation.emit()
    def deleteStation(self):
        pass

    def selectBuilding(self):
        radio = self.sender()
        if radio.isChecked():
            self.selectedBuilding = radio.value

    def filter(self):
        try:
            #empty text boxes mean dont filter, replace with None to tell sql that
            capacityMin = None if self.capacityMin.text() == '' else int(self.capacityMin.text())
            capacityMax = None if self.capacityMax.text() == '' else int(self.capacityMax.text())
            #if self.buildingNameCombobox.currentText() and self.buildingTagTextbox.text() and self.stationNameCombobox.currentText() and self.capacityMin.text() and self.capacityMax.text() and capacityMin < capacityMax:
            
            self.user.filtered = manageBuildingStationFilter(self.buildingNameCombobox.currentText(), self.buildingTagTextbox.text(), self.stationNameCombobox.currentText(), capacityMin, capacityMax)
            self.toManageBuildingStation.emit()
        except ValueError as e:
            pass

    def back(self):
        self.user.filtered = []
        self.toHome.emit()
        