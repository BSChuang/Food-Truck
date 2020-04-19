from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class SummaryDetailWindow(QtWidgets.QWidget):
    toFoodTruckSummary = QtCore.pyqtSignal()

    def __init__(self, user):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        details = getFoodTruckSummary(user.selectedTruck)
        grid = buildGrid(["Date", "Customer", "Total Purchase", "# Orders", "Food(s)"], self.formatForGrid(details))
        backButton = buildButton("Back", self.back)

        layout = buildLayout('V', [buildLabel("Summary Detail"), buildLabel("Food Truck Name: " + user.selectedTruck), grid, backButton])

        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            date = buildLabel(str(row[0]))
            customer = buildLabel(row[1])
            totalPurchase = buildLabel(str(row[2]))
            numOrders = buildLabel(str(row[3]))
            foods = buildLabel(listToString(row[4]))
            foodName = buildLabel(row[0])
            price = buildLabel(str(row[1]))
            newList.append((date, customer, totalPurchase, numOrders, foods, foodName, price))
        return newList

    def back(self):
        self.toFoodTruckSummary.emit()
