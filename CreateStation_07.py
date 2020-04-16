from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class CreateStationWindow(QtWidgets.QWidget):
    toManageBuildingStation = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        self.nameTextbox = buildTextbox()
        nameLayout = buildLayout('H', [buildLabel("Name"), self.nameTextbox])

        self.capacityTextbox = buildTextbox(True)
        capacityLayout = buildLayout('H', [buildLabel("Capacity"), self.capacityTextbox])

        self.sponsoredCombobox = buildComboBox(getBuildingNames())
        sponsoredLayout = buildLayout('H', [buildLabel("Sponsored Building"), self.sponsoredCombobox])

        hLayout = buildLayout('H', [capacityLayout, sponsoredLayout])        

        backButton = buildButton("Back", self.back)
        createButton = buildButton("Create", self.create)
        buttonsLayout = buildLayout('H', [backButton, createButton])

        layout = buildLayout('V', [buildLabel("Create Station"), nameLayout, hLayout, buttonsLayout])

        self.setLayout(layout)

    def back(self):
        self.toManageBuildingStation.emit()

    def create(self):
        insertStation(self.nameTextbox.text(), self.capacityTextbox.text(), self.sponsoredCombobox.currentText())
        self.back()