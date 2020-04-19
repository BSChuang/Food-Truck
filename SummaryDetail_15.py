from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class SummaryDetailWindow(QtWidgets.QWidget):
    toFoodTruckSummary = QtCore.pyqtSignal()

    def __init__(self, user):
        QtWidgets.QWidget.__init__(self)
        self.user = user
        self.setWindowTitle('Window')

        details = getFoodTruckSummary(user.username, user.selectedTruck)
        grid = buildGrid(["Date", "Customer", "Total Purchase", "# Orders", "Food(s)"], self.formatForGrid(details))
        backButton = buildButton("Back", self.back)

        layout = buildLayout('V', [buildLabel("Summary Detail"), buildLabel("Food Truck Name: " + user.selectedTruck + "\n"), grid, backButton])

        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            date = buildLabel(str(row[0].strftime("%d/%m/%Y")))
            customer = buildLabel(row[1])
            totalPurchase = buildLabel(str(row[2]))
            numOrders = buildLabel(str(row[3]))
            foods = buildLabel(listToString(row[4]))
            newList.append((date, customer, totalPurchase, numOrders, foods))
        return newList

    def back(self):
        self.user.selectedTruck = None
        self.toFoodTruckSummary.emit()
