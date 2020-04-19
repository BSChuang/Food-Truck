from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class OrderWindow(QtWidgets.QWidget):
    toCurrentInformation = QtCore.pyqtSignal()
    purchaseQuantities = []

    def __init__(self, user):
        self.user = user
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        menu = getTruckMenu(user.selectedTruck)
        grid = buildGrid(["Food", "Price", "Purchase Quantity"], self.formatForGrid(menu))

        self.date = buildTextbox()
        dateLayout = buildLayout('H', [buildLabel("Date (MM/DD/YYYY)"), self.date])

        backButton = buildButton("Back", self.back)
        submitButton = buildButton("Submit", self.submit)
        buttonLayout = buildLayout('H', [backButton, submitButton])

        layout = buildLayout('V', [buildLabel("Food Truck: " + user.selectedTruck), grid, buildLabel(""), dateLayout, buttonLayout])

        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            foodName = buildLabel(row[0])
            price = buildLabel(str(row[1]))
            quantityTextbox = buildTextbox(True)
            self.purchaseQuantities.append((foodName, quantityTextbox))

            newList.append((foodName, price, quantityTextbox))
        return newList

    def submit(self):
        date = datetime.strptime(self.date.text(), '%m/%d/%y')
        purchases = []
        for tup in self.purchaseQuantities:
            if tup[1].text():
                purchases.append((tup[0], tup[1]))
        
        if len(purchases) != 0:       
            submitOrder(user.username, user.selectedTruck, purchases, date)
            self.back()

    def back(self):
        self.toCurrentInformation.emit()
