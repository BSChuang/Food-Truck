import sys
from PyQt5 import QtCore, QtWidgets

from Login_01 import LoginWindow
from Register_02 import RegisterWindow
from Home_03 import HomeWindow
from ManageBuildingStationWindow_04 import ManageBuildingStationWindow
from Explore_16 import ExploreWindow
from CurrentInformation_17 import CurrentInformation
from OrderHistory_19 import OrderHistory

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

        self.homeWindow = HomeWindow(self.user.username)
        self.homeWindow.toExplore.connect(toExplore)
        self.homeWindow.toOrderHistory.connect(toOrderHistory)
        self.homeWindow.toCurrentInformation.connect(toCurrentInformation)
        self.homeWindow.toManageBuildingStation.connect(toManageBuildingStation)
        self.homeWindow.show()

    def showManageBuildingStation(self):
        def toManageBuildingStation():
            self.manageBuildingStation.close()
            self.showManageBuildingStation()

        def toHome():
            self.manageBuildingStation.close()
            self.showHome()
        
        self.manageBuildingStation = ManageBuildingStationWindow(self.user)
        self.manageBuildingStation.toHome.connect(toHome)
        self.manageBuildingStation.toManageBuildingStation.connect(toManageBuildingStation)
        self.manageBuildingStation.show()

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


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showLogin()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



""" Window class skeleton
class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')


        self.setLayout(layout)
"""