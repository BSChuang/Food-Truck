from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class CreateBuildingWindow(QtWidgets.QWidget):
    toManageBuildingStation = QtCore.pyqtSignal()
    toCreateBuilding = QtCore.pyqtSignal(str, str)
    

    def __init__(self, user, name, desc):
        self.user = user

        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')

        self.nameTextbox = buildTextbox(False, name)
        nameLayout = buildLayout('H', [buildLabel("Name"), self.nameTextbox])

        self.descTextbox = buildTextbox(False, desc)
        descLayout = buildLayout('H', [buildLabel("Description"), self.descTextbox])

        backButton = buildButton("Back", self.back)
        createButton = buildButton("Create", self.create)
        buttonsLayout = buildLayout('H', [backButton, createButton])

        layout = buildLayout('V', [buildLabel("Create Building"), nameLayout, descLayout, buildLabel("Tags"), self.buildTags(user.tags), buttonsLayout])

        self.setLayout(layout)

    def buildTags(self, tags):
        layoutList = []
        for tag in tags:
            button = QtWidgets.QPushButton("-")
            button.clicked.connect(lambda: self.removeTag(tag))
            layoutList.append(buildLayout('H', [buildLabel(tag), button]))
        
        self.newTagTextbox = buildTextbox()
        newTagButton = buildButton("+", self.addTag)
        layoutList.append(buildLayout('H', [self.newTagTextbox, newTagButton]))
        return buildLayout('V', layoutList)

    def removeTag(self, tag):
        #removeTag(self.ogbuilding, tag)
        self.user.tags.remove(tag)
        self.toCreateBuilding.emit(self.nameTextbox.text(), self.descTextbox.text())

    def addTag(self):
        text = self.newTagTextbox.text()
        if text != "" and text not in self.user.tags:
            #addTag(self.ogbuilding, self.newTagTextbox.text())
            self.user.tags.append(self.newTagTextbox.text())
            self.toCreateBuilding.emit(self.nameTextbox.text(), self.descTextbox.text())

    def back(self):
        self.user.tags = []
        self.toManageBuildingStation.emit()

    def create(self):
        names = getBuildingNames()
        if self.nameTextbox.text() not in names and self.descTextbox.text() and len(self.user.tags) > 0:
            insertBuilding(self.nameTextbox.text(), self.descTextbox.text(), self.user.tags)
            self.back()