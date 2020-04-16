from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class HomeWindow(QtWidgets.QWidget):
    toExplore = QtCore.pyqtSignal()
    toOrderHistory = QtCore.pyqtSignal()
    toCurrentInformation = QtCore.pyqtSignal()
    toManageBuildingStation = QtCore.pyqtSignal()

    def __init__(self, username):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Login Window')

        button1 = buildButton("Explore", self.explore)
        button2 = buildButton("View Order History", self.orderHistory)
        button3 = buildButton("View Current Information", self.currentInfo)
        button4 = buildButton("Manage Food Truck", self.manageFoodTruck)
        button5 = buildButton("View Food Truck Summary", self.foodTruckSummary)
        button6 = buildButton("Manage Building and Station", self.manageBuildingStation)
        button7 = buildButton("Manage Food", self.manageFood)

        userType = getUserType(username)
        if userType == "customer":
            layoutList = [button1, button2, button3]
        elif userType == "manager":
            layoutList = [button1, button2, button3, button4, button5]
        elif userType == "admin":
            layoutList = [button1, button2, button3, button6, button7]

        layout = buildLayout('V', [buildLabel("Home")] + layoutList)
        self.setLayout(layout)

    def explore(self):
        self.toExplore.emit()
    def orderHistory(self):
        self.toOrderHistory.emit()
    def currentInfo(self):
        self.toCurrentInformation.emit()
    def manageFoodTruck(self):
        pass
    def foodTruckSummary(self):
        pass
    def manageBuildingStation(self):
        self.toManageBuildingStation.emit()
    def manageFood(self):
        pass