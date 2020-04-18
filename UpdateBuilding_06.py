from PyQt5 import QtCore, QtWidgets
from Helpers import *
from Middle import *

class UpdateBuildingWindow(QtWidgets.QWidget):
    toManageBuildingStation = QtCore.pyqtSignal()
    toUpdateBuilding = QtCore.pyqtSignal()
    

    def __init__(self, user, ogbuilding):
        self.user = user
        self.ogbuilding = ogbuilding
        self.info = viewBuilding(ogbuilding) #[name, description]
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window')
        self.user.tags = getTags(ogbuilding)
        
        self.nameTextbox = buildTextbox(False, self.info[0])
        nameLayout = buildLayout('H', [buildLabel("Name"), self.nameTextbox])

        self.descTextbox = buildTextbox(False, self.info[1])
        descLayout = buildLayout('H', [buildLabel("Description"), self.descTextbox])

        backButton = buildButton("Back", self.back)
        updateButton = buildButton("Update", self.update)
        buttonsLayout = buildLayout('H', [backButton, updateButton])

        layout = buildLayout('V', [buildLabel("Update Building"), nameLayout, descLayout, buildLabel("Tags"), self.buildTags(self.user.tags), buttonsLayout])

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
        removeTag(self.ogbuilding, tag)
        self.user.tags.remove(tag)
        self.toUpdateBuilding.emit()

    def addTag(self):
        text = self.newTagTextbox.text()
        if text != "" and text not in self.user.tags:
            addTag(self.ogbuilding, self.newTagTextbox.text())
            self.user.tags.append(self.newTagTextbox.text())
            self.toUpdateBuilding.emit()

    def back(self):
        self.user.tags = []
        self.toManageBuildingStation.emit()

    def update(self):
        #names = getBuildingNames()
        #if self.nameTextbox.text() in names:
        updateBuilding(self.ogbuilding, self.nameTextbox.text(), self.descTextbox.text())
        self.back()