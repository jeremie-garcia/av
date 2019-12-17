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
        IOConfig.assiLines.append([])
        currentRow = len(IOConfig.assiLines) - 1  #indice ligne créée
        gridRow = currentRow + ASSIOFFSET

        debug("creates assi line #{}".format(currentRow))

        self.assiGridLay.addWidget(self.addAssiButton, gridRow + 1, 3, 1, 1)
        IOConfig.assiLines[-1].append(QtWidgets.QCheckBox(IOConfig))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IOConfig.assiLines[-1][0].sizePolicy().hasHeightForWidth())
        IOConfig.assiLines[-1][0].setSizePolicy(sizePolicy)
        IOConfig.assiLines[-1][0].setLayoutDirection(QtCore.Qt.LeftToRight)
        IOConfig.assiLines[-1][0].setText("")
        IOConfig.assiLines[-1][0].setChecked(False)
        IOConfig.assiLines[-1][0].setTristate(False)
        IOConfig.assiLines[-1][0].setObjectName("checkBox_"+str(currentRow-1))
        self.assiGridLay.addWidget(IOConfig.assiLines[-1][0], gridRow, 0, 1, 1, QtCore.Qt.AlignHCenter)
        IOConfig.assiLines[-1].append(QtWidgets.QComboBox(IOConfig))
        IOConfig.assiLines[-1][1].setObjectName("inputCombo_"+str(currentRow-1))
        self.assiGridLay.addWidget(IOConfig.assiLines[-1][1], gridRow, 1, 1, 1)
        IOConfig.assiLines[-1].append(QtWidgets.QComboBox(IOConfig))
        IOConfig.assiLines[-1][2].setObjectName("outputCombo_"+str(currentRow-1))
        self.assiGridLay.addWidget(IOConfig.assiLines[-1][2], gridRow, 2, 1, 1)
        IOConfig.assiLines[-1].append(QtWidgets.QPushButton(IOConfig))
        IOConfig.assiLines[-1][3].setObjectName("delAssiButton_"+str(currentRow-1))
        self.assiGridLay.addWidget(IOConfig.assiLines[-1][3], gridRow, 3)
        IOConfig.assiLines[-1][3].setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)

        IOConfig.assiLines[-1][3].setText("x")

        fillCombo(IOConfig.assiLines[-1][2], OUTPUTS)
        fillCombo(IOConfig.assiLines[-1][1], self.inputs(IOConfig))

        IOConfig.assiLines[currentRow][3].clicked.connect(lambda: self.delLine(IOConfig, IOConfig.assiLines, currentRow, self.assiGridLay, self.addAssiButton, ASSIOFFSET))
        IOConfig.assiLines[currentRow][0].stateChanged.connect(lambda s: self.lineFormula(IOConfig, s, currentRow))

    def addVarLine(self, IOConfig):
        """
        Ajoute une ligne de variables
        :param IOConfig: fenêtre de travail
        """
        IOConfig.varLines.append([])
        currentRow = len(IOConfig.varLines) - 1 #indice de la ligne qu'on crée
        gridRow = currentRow + VAROFFSET

        debug("creates var line #{}".format(currentRow))

        self.varGridLay.addWidget(self.addVarButton, gridRow + 1, 3)
        IOConfig.varLines[-1].append(QtWidgets.QLineEdit(IOConfig))
        IOConfig.varLines[-1][0].setObjectName("nomLine_"+str(currentRow-1))
        self.varGridLay.addWidget(IOConfig.varLines[-1][0], gridRow, 0)
        IOConfig.varLines[-1].append(QtWidgets.QComboBox(IOConfig))
        IOConfig.varLines[-1][1].setObjectName("typeCombo_"+str(currentRow-1))
        self.varGridLay.addWidget(IOConfig.varLines[-1][1], gridRow, 1)
        IOConfig.varLines[-1].append(QtWidgets.QLineEdit(IOConfig))
        IOConfig.varLines[-1][2].setObjectName("valeurLine_"+str(currentRow-1))
        self.varGridLay.addWidget(IOConfig.varLines[-1][2], gridRow, 2)
        IOConfig.varLines[-1].append(QtWidgets.QPushButton(IOConfig))
        IOConfig.varLines[-1][3].setObjectName("delVarButton_"+str(currentRow-1))
        self.varGridLay.addWidget(IOConfig.varLines[-1][3], gridRow, 3)
        IOConfig.varLines[-1][3].setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)

        IOConfig.varLines[-1][3].setText("x")

        self.update_inputs(IOConfig)
        fillCombo(IOConfig.varLines[-1][1], VARTYPES)

        IOConfig.varLines[currentRow][3].clicked.connect(lambda: self.delLine(IOConfig, IOConfig.varLines, currentRow, self.varGridLay, self.addVarButton, VAROFFSET))
        IOConfig.varLines[currentRow][0].editingFinished.connect(lambda: self.update_inputs(IOConfig))

    def delLine(self, IOConfig, table, n, gridLay, addButton, offset): #n indice de la ligne dans table
        """
        Supprime une ligne et recale tous les éléments suivants de gridLayout
        :param table: table des objets
        :param n: indice de la ligne à éliminer DANS LA TABLE
        :param gridLay: gridLayout associé
        :param addButton: bouton ajouter du gridLayout
        """
        debug("=======================================")
        debug("destroying line {} from {}".format(n, gridLay.objectName()))
        debug("table ({}) = {}".format(len(table), table))
        debug("asking for line {}".format(n))

        for x in table[n]:
            gridLay.removeWidget(x)
            x.deleteLater()
            debug("{} destroyed".format(x))

        gridLay.addWidget(addButton, len(table) + offset, 3)

        debug(n+1, len(table))

        for p in range(n+1,len(table)):
            for q in range(len(table[p])):
                if type(table[p][q]) == QtWidgets.QCheckBox:
                    gridLay.addWidget(table[p][q], p - 1 + offset, q, QtCore.Qt.AlignHCenter)
                else:
                    gridLay.addWidget(table[p][q], p - 1 + offset, q)

            self.varGridLay.addWidget(self.addVarButton, p + offset, 3)
            self.reconnect(table[p][3], p - 1, table, self.delLine, gridLay, addButton, offset, IOConfig)

        del table[n]
        debug("end table ({}) = {}".format(len(table), table))
        debug("=======================================")

        self.update_inputs(IOConfig)

    def reconnect(self, obj, p, table, func, gridLay, addButton, offset, IOConfig):
        """
        Reconnecte un objet à un nouveau rang
        :param obj: object à reconnecter
        :param p: nouveau rang de l'objet
        :param variables: table des objets
        :param func: fonction de suppression à utiliser
        :param gridLay: layout dans lequel est l'objet
        :param addButton: bouton ajouter du layout
        """
        obj.disconnect()
        obj.clicked.connect(lambda: func(IOConfig, table, p, gridLay, addButton, offset))
        debug("Reconnected {} to line {}".format(obj.objectName(), p))


    def inputs(self, IOConfig):
        return [_ for _ in config.SOUND_INPUTS] + [line[0].displayText() for line in IOConfig.varLines if line[0].displayText() != ""]


    def update_inputs(self, IOConfig):
        INPUTS = self.inputs(IOConfig)
        for assiLine in IOConfig.assiLines:
            if assiLine[1].__class__.__name__=="QComboBox":
                pos = assiLine[1].currentIndex()
                fillCombo(assiLine[1], INPUTS)
                assiLine[1].setCurrentIndex(pos)
        debug(INPUTS)


    def lineFormula(self, IOConfig, state, row):
        if state == 2: # si a été cochée
            self.assiGridLay.removeWidget(IOConfig.assiLines[row][1])
            IOConfig.assiLines[row][1].deleteLater()
            IOConfig.assiLines[row][1] = QtWidgets.QLineEdit(IOConfig)
            IOConfig.assiLines[row][1].setObjectName("inputFormula_" + str(row - 1))
            self.assiGridLay.addWidget(IOConfig.assiLines[row][1], row + 1, 1, 1, 1)

        else: # si a été décochée
            if IOConfig.assiLines[row][1].__class__.__name__ == "QLineEdit":
                self.assiGridLay.removeWidget(IOConfig.assiLines[row][1])
                IOConfig.assiLines[row][1].deleteLater()
            IOConfig.assiLines[row][1] = QtWidgets.QComboBox(IOConfig)
            IOConfig.assiLines[row][1].setObjectName("inputCombo_" + str(row - 1))
            self.assiGridLay.addWidget(IOConfig.assiLines[row][1], row + 1, 1, 1, 1)
            self.update_inputs(IOConfig)
            IOConfig.assiLines[row][1].setCurrentIndex(0)

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
