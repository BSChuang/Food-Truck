from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *
from datetime import datetime

class OrderWindow(QtWidgets.QWidget):
    toCurrentInformation = QtCore.pyqtSignal()

    def __init__(self, user):
        self.user = user
        self.purchaseQuantities = []
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
            self.purchaseQuantities.append((row[0], quantityTextbox, row[1]))

            newList.append((foodName, price, quantityTextbox))
        return newList

    def submit(self):
        if not self.date.text():
            return

        try:
            date = datetime.strptime(self.date.text(), '%m/%d/%Y')
        except ValueError:
            return
            
        purchases = []
        for tup in self.purchaseQuantities: # tuple(foodName, quantity, price)
            if tup[1].text() and int(tup[1].text()) >= 0:
                purchases.append((tup[0], int(tup[1].text()), tup[2]))
        
        if len(purchases) == 0:
            return
        
        if submitOrder(self.user.username, self.user.selectedTruck, purchases, date):
            self.back()
        else:
            QtWidgets.QMessageBox.about(self, "Order Error", "Order total is greater than balance.")

    def back(self):
        self.toCurrentInformation.emit()
