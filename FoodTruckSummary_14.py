from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *
from datetime import datetime

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

        self.stationNameTextbox = buildTextbox()
        stationNameLayout = buildLayout('H', [buildLabel("Station Name"), self.stationNameTextbox])

        hLayout1 = buildLayout('H', [truckNameLayout, stationNameLayout])

        self.dateMin = buildTextbox()
        self.dateMax = buildTextbox()
        dateLayout = buildLayout('H', [buildLabel("Date (MM/DD/YYYY)"), self.dateMin, buildLabel("-"), self.dateMax])

        filterButton = buildButton("Filter", self.filter)

        grid = buildGrid(["Food Truck Name", "# Total Order", "Total Revenue", "# Customer"], self.formatForGrid(self.user.filtered))

        backButton = buildButton("Back", self.back)
        detailButton = buildButton("View Detail", self.detail)
        buttonLayout = buildLayout('H', [backButton, detailButton])

        layout = buildLayout('V', [hLayout1, dateLayout, filterButton, grid, buttonLayout])

        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            truckName = buildRadioButton(row[0], lambda: self.selectFoodTruck)
            totalOrder = buildLabel(str(row[1]))
            totalRevenue = buildLabel(str(row[2]))
            numCustomer = buildLabel(str(row[3]))
            newList.append((truckName, totalOrder, totalRevenue, numCustomer))
        return newList

    def selectFoodTruck(self):
        radio = self.sender()
        if radio.isChecked():
            self.user.selectedTruck = radio.value

    def filter(self):
        try:
            dateMin = datetime.strptime(self.dateMin.text(), '%m/%d/%y')
            dateMax = datetime.strptime(self.dateMax.text(), '%m/%d/%y')
            self.user.filtered = foodTruckSummaryFilter(self.user.username, self.truckNameTextbox.text(), self.stationNameTextbox.text(), dateMin, dateMax, None, None)
            self.toFoodTruckSummary.emit()
        except ValueError:
            print("Date in wrong format")

    def back(self):
        self.user.selectedTruck = None
        self.toHome.emit()

    def detail(self):
        if self.user.selectedTruck != None:
            self.toSummaryDetail.emit()
