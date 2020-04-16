from PyQt5 import QtCore, QtWidgets

def listToString(arr):
    string = ""
    for i in range(len(arr)):
        string += arr[i]
        if i != len(arr) - 1:
            string += ", "
    return string

def buildLabel(text):
    userLabel = QtWidgets.QLabel()
    userLabel.setText(text)
    return userLabel

def buildTextbox():
    return QtWidgets.QLineEdit()

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

def buildGrid(attrNames, items):
    """
        attrNames: List of attribute names
        items: List of tuples. Each tuple should have length equal to the length of attrNames. Each item in the tuple should be a widget
    """
    layout = QtWidgets.QGridLayout()
    for i in range(len(attrNames)):
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