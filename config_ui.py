import config, sys, main
from PyQt5 import QtCore, QtWidgets

VAROFFSET = 1
ASSIOFFSET = 1

OUTPUTS = ["ellipse", "rect", "ellipse_border", "rect_border", "rect_back", "ellipse_back"]
VARTYPES = ["value", "color", "grad"]
sph = "AV-Cesar >> av-fun"

class Line():
    def __init__(self, type, tableRow, gridRow, contents):
        self.type = type
        self.tableRow = tableRow
        self.gridRow = gridRow
        self.contents = contents

class Ui_IOConfig(object):
    def setupUi(self, IOConfig, ui):
        IOConfig.assiLines, IOConfig.varLines = [], []
        IOConfig.mainWindow = ui

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
        self.confHorLay = QtWidgets.QHBoxLayout()
        self.confHorLay.setObjectName("confHorLay")
        self.confCombo = QtWidgets.QComboBox(IOConfig)
        self.confCombo.setObjectName("confCombo")
        self.confHorLay.addWidget(self.confCombo)
        self.addConfButton = QtWidgets.QPushButton(IOConfig)
        self.addConfButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addConfButton.sizePolicy().hasHeightForWidth())
        self.addConfButton.setSizePolicy(sizePolicy)
        self.addConfButton.setObjectName("addConfButton")
        self.confHorLay.addWidget(self.addConfButton)
        self.delConfButton = QtWidgets.QPushButton(IOConfig)
        self.delConfButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delConfButton.sizePolicy().hasHeightForWidth())
        self.delConfButton.setSizePolicy(sizePolicy)
        self.delConfButton.setObjectName("delConfButton")
        self.confHorLay.addWidget(self.delConfButton)
        self.confHorLay.setStretch(1, 1)
        self.confHorLay.setStretch(2, 1)
        self.genVertLay.addLayout(self.confHorLay)
        self.nameHorLay = QtWidgets.QHBoxLayout()
        self.nameHorLay.setObjectName("nameHorLay")
        self.nomConfLabel = QtWidgets.QLabel(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nomConfLabel.sizePolicy().hasHeightForWidth())
        self.nomConfLabel.setSizePolicy(sizePolicy)
        self.nomConfLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nomConfLabel.setObjectName("nomConfLabel")
        self.nameHorLay.addWidget(self.nomConfLabel)
        self.nomConfLine = QtWidgets.QLineEdit(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nomConfLine.sizePolicy().hasHeightForWidth())
        self.nomConfLine.setSizePolicy(sizePolicy)
        self.nomConfLine.setObjectName("nomConfLine")
        self.nameHorLay.addWidget(self.nomConfLine)
        self.genVertLay.addLayout(self.nameHorLay)
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

        self.resetButton = QtWidgets.QPushButton(IOConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy)
        self.resetButton.setObjectName("resetButton")
        self.buttonHorLay.addWidget(self.resetButton)

        self.genVertLay.addLayout(self.buttonHorLay)
        self.gridLayout.addLayout(self.genVertLay, 0, 0, 1, 1)

        self.retranslateUi(IOConfig)
        QtCore.QMetaObject.connectSlotsByName(IOConfig)

        self.annulerButton.clicked.connect(IOConfig.close)
        self.addAssiButton.clicked.connect(lambda: self.addAssiLine(IOConfig))
        self.addVarButton.clicked.connect(lambda: self.addVarLine(IOConfig))
        self.addConfButton.clicked.connect(lambda: self.addConfig(IOConfig))
        self.enregistrerButton.clicked.connect(lambda: config.save(self, config.winToConf(self, IOConfig)))
        self.validerButton.clicked.connect(lambda: config.valider(self, IOConfig))
        self.resetButton.clicked.connect(lambda: self.reset(IOConfig))

        IOConfig.configs = self.updateConfig()
        self.confCombo.currentIndexChanged.connect(lambda x: self.showConfig(IOConfig, x))

    def retranslateUi(self, IOConfig):
        _translate = QtCore.QCoreApplication.translate
        IOConfig.setWindowTitle(_translate("IOConfig", "Editeur de configurations"))
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
        self.resetButton.setText(_translate("IOConfig", "Reset"))
        self.addConfButton.setText(_translate("IOConfig", "+"))
        self.delConfButton.setText(_translate("IOConfig", "x"))
        self.nomConfLabel.setText(_translate("IOConfig", "Nom"))

    def addAssiLine(self, IOConfig):
        """
        Ajoute une ligne d'assignation
        :param IOConfig: fenêtre de travail
        :return:
        """
        currentRow = len(IOConfig.assiLines)  # indice ligne créée
        try: gridRow = IOConfig.assiLines[-1].gridRow + 1
        except: gridRow = 1

        main.debug(1,"creates assi line index {}, row {}".format(currentRow, gridRow))

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

        main.debug(1,"creates var line index {}, row {}".format(currentRow, gridRow))

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
        main.debug(1,"destroying {} line #{}".format(line.type, line.tableRow))

        if line.type == "ASSI":
            lines = IOConfig.assiLines
            layout = self.assiGridLay
        else:
            lines = IOConfig.varLines
            layout = self.varGridLay

        main.debug(2,"index {} in {}".format(line.tableRow, lines))
        for x in lines[line.tableRow].contents:
            layout.removeWidget(x)
            x.deleteLater()

        tableRow = line.tableRow
        gridRow = line.gridRow

        main.debug(1,"destroyed line t {}, g {}".format(tableRow, gridRow))

        for x in lines[tableRow + 1:]:
            x.tableRow -= 1
            main.debug(2,"reco {} {}".format(x.tableRow, x.gridRow))

        del lines[tableRow]
        self.update_inputs(IOConfig)

    def lineFormula(self, IOConfig, line, state):
        main.debug(2,"line t {}, g {}".format(line.tableRow, line.gridRow))

        if state == 2:  # si a été cochée
            main.debug(2,"ligne t{} : to formule".format(line.tableRow))
            self.assiGridLay.removeWidget(line.contents[1])
            line.contents[1].deleteLater()
            line.contents[1] = QtWidgets.QLineEdit(IOConfig)
            line.contents[1].setObjectName("inputFormula_" + str(line.tableRow))
            self.assiGridLay.addWidget(line.contents[1], line.gridRow, 1)

        else:  # si a été décochée
            main.debug(2,"ligne {} : fin formule".format(line.tableRow))
            if line.contents[1].__class__.__name__ == "QLineEdit":
                self.assiGridLay.removeWidget(line.contents[1])
                line.contents[1].deleteLater()
            line.contents[1] = QtWidgets.QComboBox(IOConfig)
            line.contents[1].setObjectName("inputCombo_" + str(line.tableRow))
            self.assiGridLay.addWidget(line.contents[1], line.gridRow, 1)
            self.update_inputs(IOConfig)
            line.contents[1].setCurrentIndex(0)

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

    def updateConfig(self):
        """
        Màj configs combobox
        :return: liste configs fichiers
        """
        configs = main.initConf()
        fillCombo(self.confCombo, [configs[i].name for i in range(len(configs.keys()))])
        return configs

    def addConfig(self, IOConfig):
        id = len(IOConfig.configs.keys())
        print("Creating config #{}".format(id))
        IOConfig.configs[id] = config.Configuration(id, "Config #{}".format(id))
        config.save(self, IOConfig.configs[id])
        self.updateConfig()
        self.showConfig(IOConfig, id)
        self.confCombo.setCurrentIndex(id)

    def showConfig(self, IOConfig, id):
        if id == -1: return None

        main.debug(1,"Loading config {} in {}".format(id, IOConfig.configs))
        toShow = IOConfig.configs[id]
        IOConfig.currentConf = id

        assiDict = toShow.assiDict
        varDict = toShow.varDict
        main.debug(2,assiDict, varDict)

        self.reset(IOConfig)

        for var in varDict:
            self.addVarLine(IOConfig)
            line = IOConfig.varLines[-1]
            main.debug(2,varDict[var])
            value = varDict[var].getValue()
            typeIndex = 2 if varDict[var].__class__.__name__ == "Gradation" \
                        else 1 if varDict[var].__class__.__name__ == "Color" else 0
            main.debug(2,"{}: {}".format(var, value))
            line.contents[0].setText(var)
            line.contents[1].setCurrentIndex(typeIndex)
            line.contents[2].setText(value)

        self.update_inputs(IOConfig)

        for assi in assiDict:
            if not assi == "errors":
                self.addAssiLine(IOConfig)
                line = IOConfig.assiLines[-1]
                fillCombo(line.contents[1], self.inputs(IOConfig))
                output = assi
                input = assiDict[assi]

                main.debug(2,input, output)
                line.contents[2].setCurrentIndex(line.contents[2].findText(output))

                main.debug(2,"contents : {}, searching {} => {}".format(line.contents[1].count(), input, line.contents[1].findText(input)))
                if line.contents[1].findText(input) == -1: # si formule
                    line.contents[0].toggle()
                    line.contents[1].setText(input)
                else:
                    line.contents[1].setCurrentIndex(line.contents[1].findText(input))
        
        self.nomConfLine.setText(toShow.name)
        self.confCombo.setCurrentIndex(id)


    def reset(self, IOConfig):
        if len(IOConfig.assiLines) > 0:
            self.delLine(IOConfig, IOConfig.assiLines[0])
        if len(IOConfig.varLines) > 0:
            self.delLine(IOConfig, IOConfig.varLines[0])
        if len(IOConfig.assiLines) != 0 or len(IOConfig.varLines) != 0:
            self.reset(IOConfig)

def fillCombo(combo, list):
    """
    Remplit combo avec les valeurs de list
    :param combo: comboBox
    :param list: liste des valeurs
    """
    combo.clear()
    for x in list: combo.addItem(x)

def openWindow(ui):
    IOConfig = QtWidgets.QWidget()
    uiIO = Ui_IOConfig()
    uiIO.setupUi(IOConfig, ui)
    IOConfig.show()
    uiIO.showConfig(IOConfig, ui.comboBox_2.currentIndex())
    return uiIO

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    openWindow()
    sys.exit(app.exec_())
