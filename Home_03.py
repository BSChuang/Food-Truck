from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class HomeWindow(QtWidgets.QWidget):
    toExplore = QtCore.pyqtSignal()
    toOrderHistory = QtCore.pyqtSignal()
    toCurrentInformation = QtCore.pyqtSignal()
    toManageBuildingStation = QtCore.pyqtSignal()
    toManageFood = QtCore.pyqtSignal()
    toManageFoodTruck = QtCore.pyqtSignal()
    toFoodTruckSummary = QtCore.pyqtSignal()

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
        
        # TODO Usertype now returns a list of user types because a user can belong to multiple groups
        userType = getUserType(username)
        if 'Manager' in userType:
            layoutList = [button1, button2, button3, button4, button5]
        elif 'Admin' in userType:
            layoutList = [button1, button2, button3, button6, button7]
        elif 'Customer' in userType:
            layoutList = [button1, button2, button3]

        layout = buildLayout('V', [buildLabel("Home")] + layoutList)
        self.setLayout(layout)

    def explore(self):
        self.toExplore.emit()
    def orderHistory(self):
        self.toOrderHistory.emit()
    def currentInfo(self):
        self.toCurrentInformation.emit()
    def manageFoodTruck(self):
        self.toManageFoodTruck.emit()
    def foodTruckSummary(self):
        self.toFoodTruckSummary.emit()
    def manageBuildingStation(self):
        self.toManageBuildingStation.emit()
    def manageFood(self):
        self.toManageFood.emit()