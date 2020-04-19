from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *
from datetime import datetime
import operator

class FoodTruckSummaryWindow(QtWidgets.QWidget):
    toHome = QtCore.pyqtSignal()
    toFoodTruckSummary = QtCore.pyqtSignal()
    toSummaryDetail = QtCore.pyqtSignal()

    def __init__(self, user):
        self.user = user

        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        self.truckNameTextbox = buildTextbox()
        truckNameLayout = buildLayout('H', [buildLabel("Food Truck Name (contain)"), self.truckNameTextbox])

        self.stationCombobox = buildComboBox(getStationNames())
        stationNameLayout = buildLayout('H', [buildLabel("Station Name"), self.stationCombobox])

        hLayout1 = buildLayout('H', [truckNameLayout, stationNameLayout])

        self.dateMin = buildTextbox()
        self.dateMax = buildTextbox()
        filterButton = buildButton("Filter", self.filter)
        dateLayout = buildLayout('H', [buildLabel("Date (MM/DD/YYYY)"), self.dateMin, buildLabel("-"), self.dateMax, filterButton])

        if self.user.filtered == []:
            self.user.filtered = manageFoodTruckFilter(self.user.username, None, None, None, None, False)

        grid = buildGrid(["Food Truck Name", "# Total Order", "Total Revenue", "# Customer"], self.formatForGrid(self.user.filtered), user, self)

        backButton = buildButton("Back", self.back)
        detailButton = buildButton("View Detail", self.detail)
        buttonLayout = buildLayout('H', [backButton, detailButton])

        layout = buildLayout('V', [hLayout1, dateLayout, grid, buttonLayout])

        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            truckName = buildRadioButton(row[0], self.selectFoodTruck)
            totalOrder = buildLabel(str(row[1]))
            totalRevenue = buildLabel(str(row[2]))
            numCustomer = buildLabel(str(row[3]))
            newList.append((truckName, totalOrder, totalRevenue, numCustomer))
        return newList

    def sorting(self): # Sort self.user.filtered by the self.user.sortBy and self.user.sortDir
        if self.user.sortBy == "Food Truck Name":
            self.user.filtered.sort(key=operator.itemgetter(0))
        elif self.user.sortBy == "# Total Order":
            self.user.filtered.sort(key=operator.itemgetter(1))
        elif self.user.sortBy == "Total Revenue":
            self.user.filtered.sort(key=operator.itemgetter(2))
        elif self.user.sortBy == "# Customer":
            self.user.filtered.sort(key=operator.itemgetter(3))

        if self.user.sortDir == "ASC":
            self.user.filtered.reverse()
        
        self.toFoodTruckSummary.emit()

    def selectFoodTruck(self):
        radio = self.sender()
        if radio.isChecked():
            self.user.selectedTruck = radio.value

    def filter(self):
        try:
            if self.dateMin.text() != '' :
                dateMin = datetime.strptime(self.dateMin.text(), '%m/%d/%Y')
            else :
                dateMin = None 
                
            if self.dateMax.text() != '' :
                dateMax = datetime.strptime(self.dateMax.text(), '%m/%d/%Y')
            else : dateMax = None
            
            self.user.filtered = foodTruckSummaryFilter(self.user.username, self.truckNameTextbox.text(), self.stationCombobox.currentText(), dateMin, dateMax, None, None)
            self.toFoodTruckSummary.emit()
        except ValueError:
            print("Date in wrong format")

    def back(self):
        self.user.selectedTruck = None
        self.user.filtered = []
        self.toHome.emit()

    def detail(self):
        if self.user.selectedTruck != None:
            self.toSummaryDetail.emit()
