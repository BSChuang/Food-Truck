from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class UpdateStationWindow(QtWidgets.QWidget):
    toManageBuildingStation = QtCore.pyqtSignal()

    def __init__(self, name, cap, bldg):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')
        self.bldgs = getAvailableBuilding() # available buildings + current building
        self.bldgs.insert(0, bldg)
        self.name = name
        self.nameLabel = buildLabel(self.name)
        nameLayout = buildLayout('H', [buildLabel("Name"), self.nameLabel])

        self.capacityTextbox = buildTextbox(True, str(cap))
        capacityLayout = buildLayout('H', [buildLabel("Capacity"), self.capacityTextbox])

        self.sponsoredCombobox = buildComboBox(self.bldgs)
        sponsoredLayout = buildLayout('H', [buildLabel("Sponsored Building"), self.sponsoredCombobox])

        hLayout = buildLayout('H', [capacityLayout, sponsoredLayout])        

        backButton = buildButton("Back", self.back)
        updateButton = buildButton("Update", self.update)
        buttonsLayout = buildLayout('H', [backButton, updateButton])

        layout = buildLayout('V', [buildLabel("Update Station"), nameLayout, hLayout, buttonsLayout])

        self.setLayout(layout)

    def back(self):
        self.toManageBuildingStation.emit()

    def update(self):
        if self.capacityTextbox.text() and int(self.capacityTextbox.text()) >= 0:
            updateStation(self.name, int(self.capacityTextbox.text()), self.sponsoredCombobox.currentText())
            self.back()