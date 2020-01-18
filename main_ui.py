import sys, config_ui, main, config, config_interpreter
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame, math

"""
TODO :

- ajouter curseur échelle
"""

class Drawing():
    def __init__(self, pos, scene):
        self.posX = pos[0] #position of the center
        self.posY = pos[1]
        self.scene = scene

        self.rectangle = self.scene.addRect(self.posX, self.posY, 0, 0, QtGui.QPen(QtCore.Qt.black, 5))
        self.ellipse = self.scene.addEllipse(self.posX, self.posY, 0, 0, QtGui.QPen(QtCore.Qt.black, 5))

        self.rectangle.width = 0
        self.rectangle.height = 0
        self.ellipse.width = 0
        self.ellipse.height = 0

        self.objects = {'rect': self.rectangle, 'ellipse': self.ellipse}

    def draw(self, state):
        if state == 'reset':
            for o in self.objects:
                self.resize(self.objects[o], 0, 0)
        else:
            for out in state.keys():
                if out in ["rect", "ellipse"]:
                    donnee_utile = state[out]
                    dim = donnee_utile * main.SCALE
                    self.resize(self.objects[out], dim, dim)
                elif out in ["rect_border", "ellipse_border"]:
                    donnee_utile = state[out]
                    objName = out.split("_")[0]
                    dim = donnee_utile * main.WIDTH_SCALE
                    if dim > 30:
                        pen = QtGui.QPen(QtCore.Qt.red, dim)
                    else:
                        pen = QtGui.QPen(QtCore.Qt.blue, dim)
                    self.objects[objName].setPen(pen)

            for x in ["rect", "ellipse"]:
                if x not in state.keys():
                    self.resize(self.objects[x], 0, 0)
            for x in ["rect_border", "ellipse_border"]:
                if x not in state.keys():
                    self.objects[x.split("_")[0]].setPen(QtGui.QPen(QtCore.Qt.black, 5))

    def resize(self, object, width, height):
        object.width = width
        object.height = height
        object.setRect(self.posX - object.width / 2, self.posY - object.height / 2, \
                       object.width, object.height)

class Ui_mainWindow(object):

    def __init__(self):
        self.currentConf = None
        self.currentSound = None
        self.sounds = None
        self.configs = None

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1100, 700)
        self.gridLayout = QtWidgets.QGridLayout(mainWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(mainWindow)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.comboBox_3 = QtWidgets.QComboBox(mainWindow)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_6.addWidget(self.comboBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.comboBox_4 = QtWidgets.QComboBox(mainWindow)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_7.addWidget(self.comboBox_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.comboBox_5 = QtWidgets.QComboBox(mainWindow)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_8.addWidget(self.comboBox_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(mainWindow)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(mainWindow)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.horizontalSlider = QtWidgets.QSlider(mainWindow)
        self.horizontalSlider.setMinimum(-50)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_5.addWidget(self.horizontalSlider)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.pushButton_3 = QtWidgets.QPushButton(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(mainWindow)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.pushButton_4 = QtWidgets.QPushButton(mainWindow)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_9.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(mainWindow)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_9.addWidget(self.pushButton_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QGraphicsView()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.checkBox = QtWidgets.QCheckBox(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.scene = QtWidgets.QGraphicsScene()
        #self.scene.setSceneRect(QtCore.QRectF(-50, -50, 100, 100))
        self.frame.setScene(self.scene)
        self.scene.frame = self.frame

        self.figures = self.drawScene()

        self.pushButton_3.clicked.connect(lambda: config_ui.openWindow(self))
        self.pushButton.clicked.connect(lambda: self.soundLoadPlay())
        self.comboBox.currentIndexChanged.connect(self.updateSoundFile)
        self.comboBox_2.currentIndexChanged.connect(lambda x: self.changeConfigFile(x, 0))
        self.comboBox_3.currentIndexChanged.connect(lambda x: self.changeConfigFile(x, 1))
        self.comboBox_4.currentIndexChanged.connect(lambda x: self.changeConfigFile(x, 2))
        self.comboBox_5.currentIndexChanged.connect(lambda x: self.changeConfigFile(x, 3))
        self.pushButton_2.clicked.connect(lambda: self.soundRewind())
        self.horizontalSlider.valueChanged.connect(lambda x: self.label_4.setText("{}".format(x)))
        self.pushButton_4.clicked.connect(lambda: self.frame.scale(1.2,1.2))
        self.pushButton_5.clicked.connect(lambda: self.frame.scale(0.8, 0.8))


    def drawScene(self):
        factor = 150
        figs = {}
        for x in range(2):
            for y in range(2):
                figure = Drawing([factor * (2 * x - 1), factor * (2 * y - 1)], self.scene)
                figs[x + 2 * y] = figure
        return figs

    def resetScene(self):
        self.rectangle_pen = QtGui.QPen(QtCore.Qt.black, 1)
        self.rectangle = self.scene.addRect(0, 0, 0, 0, self.rectangle_pen)
        self.ellipse_pen = QtGui.QPen(QtCore.Qt.black, 1)
        self.ellipse = self.scene.addEllipse(0, 0, 0, 0, self.ellipse_pen)

    def soundLoadPlay(self, beggining = True):
        main.debug(1,"load & play")
        self.resetScene()
        sound = main.loadSound(self, self.currentSound)
        self.soundPlay(beggining)

    def soundPlay(self, beggining = True):
        main.debug(1, "play")
        self.pushButton.clicked.disconnect()
        self.pushButton.clicked.connect(lambda: self.soundPause())
        if not beggining:
            time = pygame.mixer.music.get_pos()
        else:
            time = 0
        pygame.mixer.music.play(0, time)
        self.timer.start(self.frame_duration_ms)
        self.pushButton.setText("||")

    def soundPause(self):
        main.debug(1,"pause")
        self.pushButton.setText("|>")
        self.pushButton.clicked.disconnect()
        self.pushButton.clicked.connect(lambda: self.soundResume())
        pygame.mixer.music.pause()

    def soundResume(self):
        main.debug(1,"resume")
        #self.configUpdater()
        self.pushButton.setText("||")
        self.pushButton.clicked.disconnect()
        self.pushButton.clicked.connect(lambda: self.soundPause())
        pygame.mixer.music.unpause()

    def soundRewind(self):
        main.debug(1,"rewind")
        #self.configUpdater()
        if pygame.mixer.get_init():
            self.pushButton.clicked.disconnect()
            self.pushButton.clicked.connect(lambda: self.soundPause())
            pygame.mixer.music.stop()
            pygame.mixer.music.play()
            self.timer.start(self.frame_duration_ms)
            self.pushButton.setText("||")


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "AV-César - Visualisateur de sons"))
        self.label.setText(_translate("mainWindow", "Fichier son"))
        self.label_2.setText(_translate("mainWindow", "Configuration 1"))
        self.label_5.setText(_translate("mainWindow", "Configuration 2"))
        self.label_6.setText(_translate("mainWindow", "Configuration 3"))
        self.label_7.setText(_translate("mainWindow", "Configuration 4"))
        self.label_3.setText(_translate("mainWindow", "Décalage :"))
        self.label_4.setText(_translate("mainWindow", "0"))
        self.pushButton_3.setText(_translate("mainWindow", "Edition des configurations"))
        self.label_8.setText(_translate("mainWindow", "Zoom"))
        self.pushButton_4.setText(_translate("mainWindow", "+"))
        self.pushButton_5.setText(_translate("mainWindow", "-"))
        self.pushButton_2.setText(_translate("mainWindow", "<<"))
        self.pushButton.setText(_translate("mainWindow", "|>"))
        self.checkBox.setText(_translate("mainWindow", "Boucle"))

    def updateSoundFile(self):
        if self.sounds:
            self.currentSound = self.sounds[self.comboBox.currentText()]
            if pygame.mixer.get_init(): self.soundPause()
            self.pushButton.clicked.disconnect()
            self.pushButton.clicked.connect(lambda:self.soundLoadPlay())

    def changeConfigFile(self, index, confID):
        try:
            self.currentConf[confID] = self.configs[index]

            if type(self.currentSound).__name__ == "analyzedSound":
                self.movements[confID] = config_interpreter.Traitement(self.currentSound.donnee_brute, self.currentConf[confID])
                self.resetScene()
        except: pass

def openWindow():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QWidget()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    #sys.exit(app.exec_())
    return app

if __name__ == "__main__":
    openWindow()
