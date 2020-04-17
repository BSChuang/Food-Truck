import sys
from PyQt5 import QtCore, QtWidgets

from Login_01 import LoginWindow
from Register_02 import RegisterWindow
from Home_03 import HomeWindow
from ManageBuildingStationWindow_04 import ManageBuildingStationWindow
from Explore_16 import ExploreWindow
from CurrentInformation_17 import CurrentInformation
from OrderHistory_19 import OrderHistory
from CreateBuilding_05 import CreateBuildingWindow
from UpdateBuilding_06 import UpdateBuildingWindow
from CreateStation_07 import CreateStationWindow
from UpdateStationWindow_08 import UpdateStationWindow
from ManageFood_09 import ManageFoodWindow
from CreateFood_10 import CreateFoodWindow
from ManageFoodTruck_11 import ManageFoodTruckWindow


class Controller:
    def __init__(self):
        self.user = User()

    def showLogin(self):
        def toRegister():
            self.loginWindow.close()
            self.showRegister()

        def toHome():
            self.loginWindow.close()
            self.showHome()

        self.loginWindow = LoginWindow(self.user)
        self.loginWindow.toHome.connect(toHome)
        self.loginWindow.toRegister.connect(toRegister)
        self.loginWindow.show()

    def showRegister(self):
        def toLogin():
            self.registerWindow.close()
            self.showLogin()

        def toHome():
            self.registerWindow.close()
            self.showHome()

        self.registerWindow = RegisterWindow()
        self.registerWindow.toLogin.connect(toLogin)
        self.registerWindow.toHome.connect(toHome)
        self.registerWindow.show()

    def showHome(self):
        def toExplore():
            self.homeWindow.close()
            self.showExplore()

        def toOrderHistory():
            self.homeWindow.close()
            self.showOrderHistory()
        
        def toCurrentInformation():
            self.homeWindow.close()
            self.showCurrentInformation()

        def toManageBuildingStation():
            self.homeWindow.close()
            self.showManageBuildingStation()

        def toManageFood():
            self.homeWindow.close()
            self.showManageFood()

        def toManageFoodTruck():
            self.homeWindow.close()
            self.showManageFoodTruck()

        self.homeWindow = HomeWindow(self.user.username)
        self.homeWindow.toExplore.connect(toExplore)
        self.homeWindow.toOrderHistory.connect(toOrderHistory)
        self.homeWindow.toCurrentInformation.connect(toCurrentInformation)
        self.homeWindow.toManageBuildingStation.connect(toManageBuildingStation)
        self.homeWindow.toManageFood.connect(toManageFood)
        self.homeWindow.toManageFoodTruck.connect(toManageFoodTruck)
        self.homeWindow.show()

    def showManageBuildingStation(self):
        def toHome():
            self.manageBuildingStation.close()
            self.showHome()

        def toManageBuildingStation():
            self.manageBuildingStation.close()
            self.showManageBuildingStation()

        def toCreateBuilding():
            self.manageBuildingStation.close()
            self.showCreateBuilding()

        def toUpdateBuilding():
            self.manageBuildingStation.close()
            self.showUpdateBuilding()

        def toCreateStation():
            self.manageBuildingStation.close()
            self.showCreateStation()

        def toUpdateStation():
            self.manageBuildingStation.close()
            self.showUpdateStation()
        
        self.manageBuildingStation = ManageBuildingStationWindow(self.user)
        self.manageBuildingStation.toHome.connect(toHome)
        self.manageBuildingStation.toManageBuildingStation.connect(toManageBuildingStation)
        self.manageBuildingStation.toCreateBuilding.connect(toCreateBuilding)
        self.manageBuildingStation.toUpdateBuilding.connect(toUpdateBuilding)
        self.manageBuildingStation.toCreateStation.connect(toCreateStation)
        self.manageBuildingStation.toUpdateStation.connect(toUpdateStation)
        self.manageBuildingStation.show()

    def showCreateBuilding(self):
        def toManageBuildingStation():
            self.createBuildingWindow.close()
            self.showManageBuildingStation()

        def toCreateBuilding():
            self.createBuildingWindow.close()
            self.showCreateBuilding()

        self.createBuildingWindow = CreateBuildingWindow(self.user)
        self.createBuildingWindow.toManageBuildingStation.connect(toManageBuildingStation)
        self.createBuildingWindow.toCreateBuilding.connect(toCreateBuilding)
        self.createBuildingWindow.show()

    def showUpdateBuilding(self):
        def toManageBuildingStation():
            self.updateBuildingWindow.close()
            self.showManageBuildingStation()

        def toUpdateBuilding():
            self.updateBuildingWindow.close()
            self.showUpdateBuilding()

        self.updateBuildingWindow = UpdateBuildingWindow(self.user)
        self.updateBuildingWindow.toManageBuildingStation.connect(toManageBuildingStation)
        self.updateBuildingWindow.toUpdateBuilding.connect(toUpdateBuilding)
        self.updateBuildingWindow.show()

    def showCreateStation(self):
        def toManageBuildingStation():
            self.createStationWindow.close()
            self.showManageBuildingStation()

        self.createStationWindow = CreateStationWindow()
        self.createStationWindow.toManageBuildingStation.connect(toManageBuildingStation)
        self.createStationWindow.show()

    def showUpdateStation(self):
        def toManageBuildingStation():
            self.updateStationWindow.close()
            self.showManageBuildingStation()

        self.updateStationWindow = UpdateStationWindow()
        self.updateStationWindow.toManageBuildingStation.connect(toManageBuildingStation)
        self.updateStationWindow.show()

    def showManageFood(self):
        def toHome():
            self.manageFoodWindow.close()
            self.showHome()

        def toManageFood():
            self.manageFoodWindow.close()
            self.showManageFood()

        def toCreateFood():
            self.manageFoodWindow.close()
            self.showCreateFood()

        self.manageFoodWindow = ManageFoodWindow(self.user)
        self.manageFoodWindow.toHome.connect(toHome)
        self.manageFoodWindow.toManageFood.connect(toManageFood)
        self.manageFoodWindow.toCreateFood.connect(toCreateFood)
        self.manageFoodWindow.show()

    def showCreateFood(self):
        def toManageFood():
            self.createFoodWindow.close()
            self.showManageFood()

        self.createFoodWindow = CreateFoodWindow()
        self.createFoodWindow.toManageFood.connect(toManageFood)
        self.createFoodWindow.show()

    def showManageFoodTruck(self):
        def toHome():
            self.manageFoodTruckWindow.close()
            self.showHome()

        def toManageFoodTruck():
            self.manageFoodTruckWindow.close()
            self.showManageFoodTruck()

        self.manageFoodTruckWindow = ManageFoodTruckWindow(self.user)
        self.manageFoodTruckWindow.toHome.connect(toHome)
        self.manageFoodTruckWindow.toManageFoodTruck.connect(toManageFoodTruck)
        self.manageFoodTruckWindow.show()

    def showExplore(self):
        def toHome():
            self.exploreWindow.close()
            self.showHome()

        def toExplore(): # When filter
            self.exploreWindow.close()
            self.showExplore()

        self.exploreWindow = ExploreWindow(self.user)
        self.exploreWindow.toHome.connect(toHome)
        self.exploreWindow.toExplore.connect(toExplore)
        self.exploreWindow.show()

    def showOrderHistory(self):
        def back():
            self.orderHistory.close()
            self.showHome()
        
        self.orderHistory = OrderHistory(self.user.username)
        self.orderHistory.toHome.connect(back)
        self.orderHistory.show()
    
    def showCurrentInformation(self):
        def back():
            self.currentInformation.close()
            self.showHome()
        def order():
            self.currentInformation.close()
            # self.showOrder() IMPLEMENT THIS AFTER IMPLEMENTING ORDER
        self.currentInformation = CurrentInformation(self.user.username)
        self.currentInformation.toHome.connect(back)
        self.currentInformation.toOrder.connect(order)
        self.currentInformation.show()

class User:
    def __init__(self):
        self.username = None
        self.filtered = []
        self.tags = []


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showLogin()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



""" Window class skeleton
from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')


        self.setLayout(layout)
"""