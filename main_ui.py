import sys, config_ui, main, config, config_interpreter
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame

"""
TODO :

- ajouter curseur échelle
"""

class Ui_mainWindow(object):
    def __init__(self):
        self.currentConf = None
        self.currentSound = None
        self.sounds = None
        self.configs = None

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1018, 529)
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
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(mainWindow)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.horizontalSlider = QtWidgets.QSlider(mainWindow)
        self.horizontalSlider.setMinimum(-200)
        self.horizontalSlider.setMaximum(200)
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

        self.pushButton_3.clicked.connect(lambda: config_ui.openWindow(self))
        self.pushButton.clicked.connect(lambda: self.soundLoadPlay())
        self.comboBox.currentIndexChanged.connect(self.updateSoundFile)
        self.comboBox_2.currentIndexChanged.connect(self.changeConfigFile)
        self.pushButton_2.clicked.connect(lambda: self.soundRewind())

        self.scene = QtWidgets.QGraphicsScene()
        self.frame.setScene(self.scene)

        self.rectangle_pen = QtGui.QPen(QtCore.Qt.black, 1)
        self.rectangle = self.scene.addRect(0,0,0,0, self.rectangle_pen)
        self.ellipse_pen = QtGui.QPen(QtCore.Qt.black, 1)
        self.ellipse = self.scene.addEllipse(0,0,0,0, self.ellipse_pen)

        self.OBJECTS = {"ellipse": self.ellipse, "rect": self.rectangle}

    """def soundTimeCoggntrol(self, type):
        main.initConf()
        main.showConfig(self)
        if type == 0: #resume song

        elif type == 1: #pause song

        elif type == 2: #first load & play"""

    def resetScene(self):
        self.rectangle_pen = QtGui.QPen(QtCore.Qt.black, 1)
        self.rectangle = self.scene.addRect(0, 0, 0, 0, self.rectangle_pen)
        self.ellipse_pen = QtGui.QPen(QtCore.Qt.black, 1)
        self.ellipse = self.scene.addEllipse(0, 0, 0, 0, self.ellipse_pen)

    def soundLoadPlay(self, beggining = True):
        main.debug(1,"load & play")
        self.resetScene()
        sound = main.loadSound(self, self.currentSound, self.currentConf)
        self.soundPlay(sound, beggining)

    def soundPlay(self, sound, beggining = True):
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
        self.pushButton.clicked.disconnect()
        self.pushButton.clicked.connect(lambda: self.soundPause())
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        self.timer.start(self.frame_duration_ms)
        self.pushButton.setText("||")


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "mainWindow"))
        self.label.setText(_translate("mainWindow", "Fichier son"))
        self.label_2.setText(_translate("mainWindow", "Configuration"))
        self.label_3.setText(_translate("mainWindow", "Synchro"))
        self.pushButton_3.setText(_translate("mainWindow", "Edition des configurations"))
        self.pushButton_2.setText(_translate("mainWindow", "<<"))
        self.pushButton.setText(_translate("mainWindow", "|>"))
        self.checkBox.setText(_translate("mainWindow", "Boucle"))

    def updateSoundFile(self, *args):
        if self.sounds:
            self.currentSound = self.sounds[self.comboBox.currentText()]
            self.pushButton.clicked.disconnect()
            self.pushButton.clicked.connect(lambda:self.soundLoadPlay())

    def changeConfigFile(self, index):
        if index != -1 and self.configs:
            self.currentConf = self.configs[index]

            if type(self.currentSound).__name__ == "analyzedSound":
                self.movements = config_interpreter.Traitement(self.currentSound.donnee_brute, self.currentConf)
                self.resetScene()

def openWindow():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QWidget()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    ui.updateConfigs.connect(ui.draw())
    #sys.exit(app.exec_())
    return app

if __name__ == "__main__":
    openWindow()
