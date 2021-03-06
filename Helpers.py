from PyQt5 import QtCore, QtWidgets, QtGui
from functools import partial

def listToString(arr):
    string = ""
    for i in range(len(arr)):
        string += arr[i]
        if i != len(arr) - 1:
            string += ", "
    return string

def threeListToString(arr):
    string = ""
    for i in range(len(arr)):
        string += arr[i]
        if i != len(arr) - 1:
            string += ", "
            if i % 3 == 2:
                string += "\n"
    return string

def buildList(strings, selectedIndices):
    li = QtWidgets.QListWidget()
    li.addItems(strings)
    li.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
    if selectedIndices != None:
        for index in selectedIndices:
            li.item(index).setSelected(True)
    return li

def buildLabel(text):
    userLabel = QtWidgets.QLabel()
    userLabel.setText(text)
    return userLabel

def buildTextbox(onlyInt=False, defStr = ''):
    textbox = QtWidgets.QLineEdit(defStr)

    if onlyInt:
        textbox.setValidator(QtGui.QIntValidator())
    return textbox

def buildButton(text, func):
    button = QtWidgets.QPushButton(text)
    button.clicked.connect(func)
    return button

def buildRadioButton(text, func, isChecked=False):
    radio = QtWidgets.QRadioButton(text)
    radio.setChecked(isChecked)
    radio.value = text
    radio.toggled.connect(func)
    return radio

def buildComboBox(items):
    comboBox = QtWidgets.QComboBox()
    comboBox.addItems(items)
    return comboBox

def buildGrid(attrNames, items, user=None, window=None):
    """
        attrNames: List of attribute names
        items: List of tuples. Each tuple should have length equal to the length of attrNames. Each item in the tuple should be a widget
    """

    def sortBy(attrName):
        if user.sortBy == attrName:
            dic = {None: "ASC", "ASC": "DESC", "DESC": "ASC"}
            user.sortDir = dic[user.sortDir]
        else:    
            user.sortBy = attrName
        window.sorting()

    layout = QtWidgets.QGridLayout()
    for i in range(len(attrNames)):
        if user != None:
            sortButton = buildButton(attrNames[i], partial(lambda i: sortBy(attrNames[i]), i=i))
            layout.addWidget(sortButton, 0, i)
        else:
            layout.addWidget(buildLabel(attrNames[i]), 0, i)

        for j in range(len(items)):
            if type(items[j][i]) == QtWidgets.QHBoxLayout or type(items[j][i]) == QtWidgets.QVBoxLayout:
                layout.addLayout(items[j][i], j+1, i)
            else:    
                layout.addWidget(items[j][i], j+1, i)
    return layout

def buildLayout(layoutType, items):
    if layoutType == "H":
        layout = QtWidgets.QHBoxLayout()
    elif layoutType == "V":
        layout = QtWidgets.QVBoxLayout()
    else:
        layout = QtWidgets.QGridLayout()

    for item in items:
        if type(item) == QtWidgets.QHBoxLayout or type(item) == QtWidgets.QVBoxLayout or type(item) == QtWidgets.QGridLayout:
            layout.addLayout(item)
        else:
            layout.addWidget(item)

    return layout