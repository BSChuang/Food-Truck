import sys
from PyQt5 import QtCore, QtWidgets
from Login_01 import LoginWindow
from Register_02 import RegisterWindow
from Home_03 import HomeWindow
from ManageBuildingStationWindow_04 import ManageBuildingStationWindow
from CreateBuilding_05 import CreateBuildingWindow
from UpdateBuilding_06 import UpdateBuildingWindow
from CreateStation_07 import CreateStationWindow
from UpdateStationWindow_08 import UpdateStationWindow
from ManageFood_09 import ManageFoodWindow
from CreateFood_10 import CreateFoodWindow
from ManageFoodTruck_11 import ManageFoodTruckWindow
from CreateFoodTruck_12 import CreateFoodTruckWindow
from UpdateFoodTruck_13 import UpdateFoodTruckWindow
from FoodTruckSummary_14 import FoodTruckSummaryWindow
from SummaryDetail_15 import SummaryDetailWindow
from Explore_16 import ExploreWindow
from CurrentInformation_17 import CurrentInformation
from Order_18 import OrderWindow
from OrderHistory_19 import OrderHistory
from Middle import exploreFilter, manageBuildingStationFilter, manageFoodTruckFilter, foodTruckSummaryFilter, manageFoodFilter

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

        self.registerWindow = RegisterWindow(self.user)
        self.registerWindow.toLogin.connect(toLogin)
        self.registerWindow.toHome.connect(toHome)
        self.registerWindow.show()

    def showHome(self):
        def toExplore():
            self.homeWindow.close()
            #show all data
            self.user.filtered = exploreFilter(None, None, None, None, None)
            self.showExplore()

        def toOrderHistory():
            self.homeWindow.close()
            self.showOrderHistory()

        def toCurrentInformation():
            self.homeWindow.close()
            self.showCurrentInformation()

        def toManageBuildingStation():
            self.homeWindow.close()
            #show def data
            self.user.filtered = manageBuildingStationFilter(None, None, None, None, None)
            self.showManageBuildingStation()

        def toManageFood():
            self.homeWindow.close()
            self.showManageFood()

        def toManageFoodTruck():
            self.homeWindow.close()
            # show all data when navigating to this
            self.user.filtered = manageFoodTruckFilter(self.user.username, None, None, None, None, False)
            self.showManageFoodTruck()

        def toFoodTruckSummary():
            self.homeWindow.close()
            self.user.filtered = foodTruckSummaryFilter(self.user.username, None, None, None, None, None, None)
            self.showFoodTruckSummary()

        self.homeWindow = HomeWindow(self.user.username)
        self.homeWindow.toExplore.connect(toExplore)
        self.homeWindow.toOrderHistory.connect(toOrderHistory)
        self.homeWindow.toCurrentInformation.connect(toCurrentInformation)
        self.homeWindow.toManageBuildingStation.connect(toManageBuildingStation)
        self.homeWindow.toManageFood.connect(toManageFood)
        self.homeWindow.toManageFoodTruck.connect(toManageFoodTruck)
        self.homeWindow.toFoodTruckSummary.connect(toFoodTruckSummary)
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

        def toUpdateBuilding(bldg):
            self.manageBuildingStation.close()
            self.showUpdateBuilding(bldg)

        def toCreateStation():
            self.manageBuildingStation.close()
            self.showCreateStation()

        def toUpdateStation(name, cap, bldg):
            self.manageBuildingStation.close()
            self.showUpdateStation(name, cap, bldg)

        self.manageBuildingStation = ManageBuildingStationWindow(self.user)
        self.manageBuildingStation.toHome.connect(toHome)
        self.manageBuildingStation.toManageBuildingStation.connect(toManageBuildingStation)
        self.manageBuildingStation.toCreateBuilding.connect(toCreateBuilding)
        self.manageBuildingStation.toUpdateBuilding.connect(toUpdateBuilding)
        self.manageBuildingStation.toCreateStation.connect(toCreateStation)
        self.manageBuildingStation.toUpdateStation.connect(toUpdateStation)
        self.manageBuildingStation.show()

    def showCreateBuilding(self, name = '', desc = ''):
        def toManageBuildingStation():
            self.createBuildingWindow.close()
            self.user.filtered = manageBuildingStationFilter(None, None, None, None, None)
            self.showManageBuildingStation()

        def toCreateBuilding(name, desc):
            self.createBuildingWindow.close()
            self.user.filtered = manageBuildingStationFilter(None, None, None, None, None)
            self.showCreateBuilding(name, desc)

        self.createBuildingWindow = CreateBuildingWindow(self.user, name, desc)
        self.createBuildingWindow.toManageBuildingStation.connect(toManageBuildingStation)
        self.createBuildingWindow.toCreateBuilding.connect(toCreateBuilding)
        self.createBuildingWindow.show()

    def showUpdateBuilding(self, bldg):
        def toManageBuildingStation():
            self.updateBuildingWindow.close()
            self.user.filtered = manageBuildingStationFilter(None, None, None, None, None)
            self.showManageBuildingStation()

        def toUpdateBuilding():
            self.updateBuildingWindow.close()
            self.user.filtered = manageBuildingStationFilter(None, None, None, None, None)
            self.showUpdateBuilding(bldg)

        self.updateBuildingWindow = UpdateBuildingWindow(self.user, bldg)
        self.updateBuildingWindow.toManageBuildingStation.connect(toManageBuildingStation)
        self.updateBuildingWindow.toUpdateBuilding.connect(toUpdateBuilding)
        self.updateBuildingWindow.show()

    def showCreateStation(self):
        def toManageBuildingStation():
            self.createStationWindow.close()
            self.user.filtered = manageBuildingStationFilter(None, None, None, None, None)
            self.showManageBuildingStation()

        self.createStationWindow = CreateStationWindow()
        self.createStationWindow.toManageBuildingStation.connect(toManageBuildingStation)
        self.createStationWindow.show()

    def showUpdateStation(self, name, cap, bldg):
        def toManageBuildingStation():
            self.updateStationWindow.close()
            self.user.filtered = manageBuildingStationFilter(None, None, None, None, None)
            self.showManageBuildingStation()

        self.updateStationWindow = UpdateStationWindow(name, cap, bldg)
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
            self.user.filtered = manageFoodFilter(None, None, None)
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

        def toCreateFoodTruck():
            self.manageFoodTruckWindow.close()
            self.showCreateFoodTruck()

        def toUpdateFoodTruck(name, station):
            self.manageFoodTruckWindow.close()
            self.showUpdateFoodTruck(name, station)

        self.manageFoodTruckWindow = ManageFoodTruckWindow(self.user)
        self.manageFoodTruckWindow.toHome.connect(toHome)
        self.manageFoodTruckWindow.toManageFoodTruck.connect(toManageFoodTruck)
        self.manageFoodTruckWindow.toCreateFoodTruck.connect(toCreateFoodTruck)
        self.manageFoodTruckWindow.toUpdateFoodTruck.connect(toUpdateFoodTruck)
        self.manageFoodTruckWindow.show()

    def showCreateFoodTruck(self, name = '', station = '', assignedStaff = None):
        def toManageFoodTruck():
            self.createFoodTruckWindow.close()
            self.user.filtered = manageFoodTruckFilter(self.user.username, None, None, None, None, False)
            self.showManageFoodTruck()

        def toCreateFoodTruck(name, station, assignedStaff):
            self.createFoodTruckWindow.close()
            self.showCreateFoodTruck(name, station, assignedStaff)

        self.createFoodTruckWindow = CreateFoodTruckWindow(self.user, name, station, assignedStaff)
        self.createFoodTruckWindow.toCreateFoodTruck.connect(toCreateFoodTruck)
        self.createFoodTruckWindow.toManageFoodTruck.connect(toManageFoodTruck)
        self.createFoodTruckWindow.show()

    def showUpdateFoodTruck(self, name = '', station = '', assignedStaff = None):
        def toManageFoodTruck():
            self.updateFoodTruckWindow.close()
            self.user.filtered = manageFoodTruckFilter(self.user.username, None, None, None, None, False)
            self.showManageFoodTruck()
        
        def toUpdateFoodTruck(name, station, assignedStaff):
            self.updateFoodTruckWindow.close()
            self.showUpdateFoodTruck(name, station, assignedStaff)

        self.updateFoodTruckWindow = UpdateFoodTruckWindow(self.user, name, station, assignedStaff)
        self.updateFoodTruckWindow.toUpdateFoodTruck.connect(toUpdateFoodTruck)
        self.updateFoodTruckWindow.toManageFoodTruck.connect(toManageFoodTruck)
        self.updateFoodTruckWindow.show()

    def showFoodTruckSummary(self):
        def toHome():
            self.foodTruckSummaryWindow.close()
            self.showHome()

        def toFoodTruckSummary():
            self.foodTruckSummaryWindow.close()
            self.showFoodTruckSummary()

        def toSummaryDetail():
            self.foodTruckSummaryWindow.close()
            self.showSummaryDetail()

        self.foodTruckSummaryWindow = FoodTruckSummaryWindow(self.user)
        self.foodTruckSummaryWindow.toHome.connect(toHome)
        self.foodTruckSummaryWindow.toFoodTruckSummary.connect(toFoodTruckSummary)
        self.foodTruckSummaryWindow.toSummaryDetail.connect(toSummaryDetail)
        self.foodTruckSummaryWindow.show()

    def showSummaryDetail(self):
        def toFoodTruckSummary():
            self.summaryDetailWindow.close()
            self.showFoodTruckSummary()

        self.summaryDetailWindow = SummaryDetailWindow(self.user)
        self.summaryDetailWindow.toFoodTruckSummary.connect(toFoodTruckSummary)
        self.summaryDetailWindow.show()

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

    def showCurrentInformation(self):
        def back():
            self.currentInformation.close()
            self.showHome()

        def order():
            self.currentInformation.close()
            self.showOrder()

        self.currentInformation = CurrentInformation(self.user)
        self.currentInformation.toHome.connect(back)
        self.currentInformation.toOrder.connect(order)
        self.currentInformation.show()

    def showOrder(self):
        def toCurrentInformation():
            self.order.close()
            self.showCurrentInformation()

        self.order = OrderWindow(self.user)
        self.order.toCurrentInformation.connect(toCurrentInformation)
        self.order.show()

    def showOrderHistory(self):
        def back():
            self.orderHistory.close()
            self.showHome()

        self.orderHistory = OrderHistory(self.user.username)
        self.orderHistory.toHome.connect(back)
        self.orderHistory.show()

class User:
    def __init__(self):
        self.username = None
        self.filtered = []
        self.tags = []
        self.menuItems = []
        self.selectedTruck = None
        self.sortBy = None
        self.sortDir = None


def main():
    QtWidgets.QApplication.setStyle('Fusion')
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
