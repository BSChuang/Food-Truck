from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class OrderHistory(QtWidgets.QWidget):
    toHome = QtCore.pyqtSignal()
    
    def __init__(self, username):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Order History')

        history = getOrderHistory(username)
        grid = buildGrid(["Date", "OrderID", "Order Total", "Food(s)", "Food Quantity"], self.formatForGrid(history))
        self.button1 = buildButton("Back", self.back)

        layout = buildLayout("V", [buildLabel("Order History"), grid, self.button1])
        self.setLayout(layout)

    def formatForGrid(self, rows):
        newList = []
        for row in rows:
            date = buildLabel(str(row[0]))
            orderId = buildLabel(str(row[1]))
            orderTotal = buildLabel(str(row[2]))
            foods = buildLabel(str(listToString(row[3])))
            quantity = buildLabel(str(row[4]))
            newList.append((date, orderId, orderTotal, foods, quantity))
        return newList
        
    def back(self):
        self.toHome.emit()