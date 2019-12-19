import config, sys
from PyQt5 import QtCore, QtWidgets

"""
TODO:

- Ajouter choix nom conf + enregistrer avec ce nom dans un dossier séparé 'configurations'
- bug suppression ligne + passage mode fonction
"""

DEBUG = False
VAROFFSET = 1
ASSIOFFSET = 1

OUTPUTS = ["size", "px", "py", "vibration", "color"]
VARTYPES = ["value", "color", "grad"]

class Line():
    def __init__(self, type, tableRow, gridRow, contents):
        self.type = type
        self.tableRow = tableRow
        self.gridRow = gridRow
        self.contents = contents


class Ui_IOConfig(object):
    def setupUi(self, IOConfig):
        IOConfig.assiLines, IOConfig.varLines = [], []

        IOConfig.setObjectName("IOConfig")
        IOConfig.resize(503, 305)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IOConfig.sizePolicy().hasHeightForWidth())
        IOConfig.setSizePolicy(sizePolicy)
        IOConfig.setWindowOpacity(1.0)
        self.gridLayout = QtWidgets.QGridLayout(IOConfig)
        self.gridLayout.setObjectName("gridLayout")
        self.genVertLay = QtWidgets.QVBoxLayout()
        self.genVertLay.setObjectName("genVertLay")
        self.assiVertLay = QtWidgets.QVBoxLayout()
        self.assiVertLay.setObjectName("assiVertLay")
        self.line_4 = QtWidgets.QFrame(IOConfig)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.assiVertLay.addWidget(self.line_4)
        self.assiLabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assiLabel.sizePolicy().hasHeightForWidth())
        self.assiLabel.setSizePolicy(sizePolicy)
        self.assiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.assiLabel.setObjectName("assiLabel")
        self.assiVertLay.addWidget(self.assiLabel)
        self.line_3 = QtWidgets.QFrame(IOConfig)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.assiVertLay.addWidget(self.line_3)
        self.assiGridLay = QtWidgets.QGridLayout()
        self.assiGridLay.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.assiGridLay.setObjectName("assiGridLay")
        self.sortielabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortielabel.sizePolicy().hasHeightForWidth())
        self.sortielabel.setSizePolicy(sizePolicy)
        self.sortielabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sortielabel.setObjectName("sortielabel")
        self.assiGridLay.addWidget(self.sortielabel, 0, 2, 1, 1)
        self.addAssiButton = QtWidgets.QPushButton(IOConfig)
        self.addAssiButton.setObjectName("addAssiButton")
        self.assiGridLay.addWidget(self.addAssiButton, 1, 3, 1, 1)
        self.entreelabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entreelabel.sizePolicy().hasHeightForWidth())
        self.entreelabel.setSizePolicy(sizePolicy)
        self.entreelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.entreelabel.setObjectName("entreelabel")
        self.assiGridLay.addWidget(self.entreelabel, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.assiGridLay.addWidget(self.label, 0, 0, 1, 1)
        self.assiVertLay.addLayout(self.assiGridLay)
        self.genVertLay.addLayout(self.assiVertLay)
        self.varVertLay = QtWidgets.QVBoxLayout()
        self.varVertLay.setObjectName("varVertLay")
        self.line = QtWidgets.QFrame(IOConfig)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.varVertLay.addWidget(self.line)
        self.varLabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.varLabel.sizePolicy().hasHeightForWidth())
        self.varLabel.setSizePolicy(sizePolicy)
        self.varLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.varLabel.setObjectName("varLabel")
        self.varVertLay.addWidget(self.varLabel)
        self.line_2 = QtWidgets.QFrame(IOConfig)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.varVertLay.addWidget(self.line_2)
        self.varGridLay = QtWidgets.QGridLayout()
        self.varGridLay.setObjectName("varGridLay")
        self.addVarButton = QtWidgets.QPushButton(IOConfig)
        self.addVarButton.setObjectName("addVarButton")
        self.varGridLay.addWidget(self.addVarButton, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.valeurLabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valeurLabel.sizePolicy().hasHeightForWidth())
        self.valeurLabel.setSizePolicy(sizePolicy)
        self.valeurLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.valeurLabel.setObjectName("valeurLabel")
        self.varGridLay.addWidget(self.valeurLabel, 0, 2, 1, 1)
        self.typeLabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeLabel.sizePolicy().hasHeightForWidth())
        self.typeLabel.setSizePolicy(sizePolicy)
        self.typeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.typeLabel.setObjectName("typeLabel")
        self.varGridLay.addWidget(self.typeLabel, 0, 1, 1, 1)
        self.nomLabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nomLabel.sizePolicy().hasHeightForWidth())
        self.nomLabel.setSizePolicy(sizePolicy)
        self.nomLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nomLabel.setObjectName("nomLabel")
        self.varGridLay.addWidget(self.nomLabel, 0, 0, 1, 1)
        self.varVertLay.addLayout(self.varGridLay)
        self.genVertLay.addLayout(self.varVertLay)
        self.buttonHorLay = QtWidgets.QHBoxLayout()
        self.buttonHorLay.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.buttonHorLay.setObjectName("buttonHorLay")
        self.annulerButton = QtWidgets.QPushButton(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.annulerButton.sizePolicy().hasHeightForWidth())
        self.annulerButton.setSizePolicy(sizePolicy)
        self.annulerButton.setObjectName("annulerButton")
        self.buttonHorLay.addWidget(self.annulerButton)
        self.enregistrerButton = QtWidgets.QPushButton(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enregistrerButton.sizePolicy().hasHeightForWidth())
        self.enregistrerButton.setSizePolicy(sizePolicy)
        self.enregistrerButton.setObjectName("enregistrerButton")
        self.buttonHorLay.addWidget(self.enregistrerButton)
        self.validerButton = QtWidgets.QPushButton(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validerButton.sizePolicy().hasHeightForWidth())
        self.validerButton.setSizePolicy(sizePolicy)
        self.validerButton.setObjectName("validerButton")
        self.buttonHorLay.addWidget(self.validerButton)
        self.genVertLay.addLayout(self.buttonHorLay)
        self.gridLayout.addLayout(self.genVertLay, 0, 0, 1, 1)

        self.retranslateUi(IOConfig)
        QtCore.QMetaObject.connectSlotsByName(IOConfig)

        self.annulerButton.clicked.connect(IOConfig.close)
        self.addAssiButton.clicked.connect(lambda: self.addAssiLine(IOConfig))
        self.addVarButton.clicked.connect(lambda: self.addVarLine(IOConfig))
        self.enregistrerButton.clicked.connect(lambda: config.save(IOConfig))
        self.validerButton.clicked.connect(lambda: config.valider(IOConfig))

        self.addAssiLine(IOConfig)
        self.addVarLine(IOConfig)

    def retranslateUi(self, IOConfig):
        _translate = QtCore.QCoreApplication.translate
        IOConfig.setWindowTitle(_translate("IOConfig", "I/O Configurator"))
        self.assiLabel.setText(_translate("IOConfig", "Assignations"))
        self.sortielabel.setText(_translate("IOConfig", "Sortie"))
        self.addAssiButton.setText(_translate("IOConfig", "+"))
        self.entreelabel.setText(_translate("IOConfig", "Entrée"))
        self.label.setText(_translate("IOConfig", "f(x)"))
        self.varLabel.setText(_translate("IOConfig", "Variables"))
        self.addVarButton.setText(_translate("IOConfig", "+"))
        self.valeurLabel.setText(_translate("IOConfig", "Valeur"))
        self.typeLabel.setText(_translate("IOConfig", "Type"))
        self.nomLabel.setText(_translate("IOConfig", "Nom"))
        self.annulerButton.setText(_translate("IOConfig", "Annuler"))
        self.enregistrerButton.setText(_translate("IOConfig", "Enregistrer"))
        self.validerButton.setText(_translate("IOConfig", "Valider"))

    def addAssiLine(self, IOConfig):
        """
        Ajoute une ligne d'assignation
        :param IOConfig: fenêtre de travail
        :return:
        """
        currentRow = len(IOConfig.assiLines)  # indice ligne créée
        try: gridRow = IOConfig.assiLines[-1].gridRow + 1
        except: gridRow = 1

        debug("creates assi line index {}, row {}".format(currentRow, gridRow))

        IOConfig.assiLines.append(Line("ASSI", currentRow, gridRow, []))
        contents = IOConfig.assiLines[-1].contents

        self.assiGridLay.addWidget(self.addAssiButton, gridRow + 1, 3)
        IOConfig.assiLines[-1].contents.append(QtWidgets.QCheckBox(IOConfig))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(contents[0].sizePolicy().hasHeightForWidth())
        contents[0].setSizePolicy(sizePolicy)
        contents[0].setLayoutDirection(QtCore.Qt.LeftToRight)
        contents[0].setText("")
        contents[0].setChecked(False)
        contents[0].setTristate(False)
        contents[0].setObjectName("checkBox_" + str(currentRow - 1))
        self.assiGridLay.addWidget(contents[0], gridRow, 0, QtCore.Qt.AlignHCenter)
        contents.append(QtWidgets.QComboBox(IOConfig))
        contents[1].setObjectName("inputCombo_" + str(currentRow - 1))
        self.assiGridLay.addWidget(contents[1], gridRow, 1)
        contents.append(QtWidgets.QComboBox(IOConfig))
        contents[2].setObjectName("outputCombo_" + str(currentRow - 1))
        self.assiGridLay.addWidget(contents[2], gridRow, 2)
        contents.append(QtWidgets.QPushButton(IOConfig))
        contents[3].setObjectName("delAssiButton_" + str(currentRow - 1))
        self.assiGridLay.addWidget(contents[3], gridRow, 3)
        contents[3].setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)

        debug("assiLines index t {}, g {}".format(currentRow, gridRow))

        contents[3].setText("x")

        fillCombo(contents[2], OUTPUTS)
        fillCombo(contents[1], self.inputs(IOConfig))

        addedLine = IOConfig.assiLines[-1]
        contents[3].clicked.connect(lambda: self.delLine(IOConfig, addedLine))
        contents[0].stateChanged.connect(lambda s: self.lineFormula(IOConfig, addedLine, s))

    def addVarLine(self, IOConfig):
        """
        Ajoute une ligne de variables
        :param IOConfig: fenêtre de travail
        """
        currentRow = len(IOConfig.varLines)  # indice ligne créée
        try:
            gridRow = IOConfig.varLines[-1].gridRow + 1
        except:
            gridRow = 1

        debug("creates var line index {}, row {}".format(currentRow, gridRow))

        IOConfig.varLines.append(Line("VAR", currentRow, gridRow, []))
        contents = IOConfig.varLines[-1].contents

        self.varGridLay.addWidget(self.addVarButton, gridRow + 1, 3)
        contents.append(QtWidgets.QLineEdit(IOConfig))
        contents[0].setObjectName("nomLine_"+str(currentRow - 1))
        self.varGridLay.addWidget(contents[0], gridRow, 0)
        contents.append(QtWidgets.QComboBox(IOConfig))
        contents[1].setObjectName("typeCombo_"+str(currentRow - 1))
        self.varGridLay.addWidget(contents[1], gridRow, 1)
        contents.append(QtWidgets.QLineEdit(IOConfig))
        contents[2].setObjectName("valeurLine_"+str(currentRow - 1))
        self.varGridLay.addWidget(contents[2], gridRow, 2)
        contents.append(QtWidgets.QPushButton(IOConfig))
        contents[3].setObjectName("delVarButton_"+str(currentRow - 1))
        self.varGridLay.addWidget(contents[3], gridRow, 3)
        contents[3].setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)

        contents[3].setText("x")

        self.update_inputs(IOConfig)
        fillCombo(contents[1], VARTYPES)

        line = IOConfig.varLines[-1]
        contents[3].clicked.connect(lambda: self.delLine(IOConfig, line))
        contents[0].editingFinished.connect(lambda: self.update_inputs(IOConfig))

    def delLine(self, IOConfig, line):
        """
        Supprime une ligne de la fenêtre
        :param IOConfig: fenêtre
        :param line: ligne à supprimer
        """
        debug("destroying {} line #{}".format(line.type, line.tableRow))

        if line.type == "ASSI":
            lines = IOConfig.assiLines
            layout = self.assiGridLay
        else:
            lines = IOConfig.varLines
            layout = self.varGridLay

        for x in lines[line.tableRow].contents:
            layout.removeWidget(x)
            x.deleteLater()

        tableRow = line.tableRow
        gridRow = line.gridRow

        debug("destroyed line t {}, g {}".format(tableRow, gridRow))

        for x in lines[tableRow + 1:]:
            x.tableRow -= 1
            debug("reco {} {}".format(x.tableRow, x.gridRow))

        del lines[tableRow]
        self.update_inputs(IOConfig)


    def inputs(self, IOConfig):
        return [_ for _ in config.SOUND_INPUTS] + [line.contents[0].displayText() for line in IOConfig.varLines if
                                                   not line.contents[0].displayText() == ""]


    def update_inputs(self, IOConfig):
        INPUTS = self.inputs(IOConfig)
        for assiLine in IOConfig.assiLines:
            if assiLine.contents[1].__class__.__name__=="QComboBox":
                pos = assiLine.contents[1].currentIndex()
                fillCombo(assiLine.contents[1], INPUTS)
                assiLine.contents[1].setCurrentIndex(pos)


    def lineFormula(self, IOConfig, line, state):
        debug("line t {}, g {}".format(line.tableRow, line.gridRow))

        if state == 2: # si a été cochée
            debug("ligne t{} : to formule".format(line.tableRow))
            self.assiGridLay.removeWidget(line.contents[1])
            line.contents[1].deleteLater()
            line.contents[1] = QtWidgets.QLineEdit(IOConfig)
            line.contents[1].setObjectName("inputFormula_" + str(line.tableRow))
            self.assiGridLay.addWidget(line.contents[1], line.gridRow, 1)

        else: # si a été décochée
            debug("ligne {} : fin formule".format(line.tableRow))
            if line.contents[1].__class__.__name__ == "QLineEdit":
                self.assiGridLay.removeWidget(line.contents[1])
                line.contents[1].deleteLater()
            line.contents[1] = QtWidgets.QComboBox(IOConfig)
            line.contents[1].setObjectName("inputCombo_" + str(line.tableRow))
            self.assiGridLay.addWidget(line.contents[1], line.gridRow, 1)
            self.update_inputs(IOConfig)
            line.contents[1].setCurrentIndex(0)

def fillCombo(combo, list):
    """
    Remplit combo avec les valeurs de list
    :param combo: comboBox
    :param list: liste des valeurs
    """
    combo.clear()
    for x in list: combo.addItem(x)

def debug(*args):
    if DEBUG: print(*args)

def openWindow():
    app = QtWidgets.QApplication(sys.argv)
    IOConfig = QtWidgets.QWidget()
    ui = Ui_IOConfig()
    ui.setupUi(IOConfig)
    IOConfig.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    openWindow()
