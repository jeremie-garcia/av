"""Sound visualization.

This module allows the visualization of a sound and its variations
on a scalable graphics view"""

import math

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPen, QBrush, QColor
import sound_analyzer
import pygame
import sys
import figures
from PyQt5.QtGui import QPen, QColor,  QGradient

# constants
WIDTH = 800  # Initial window width (pixels)
HEIGHT = 450  # Initial window height (pixels)
ANIMATION_DELAY = 50  # milliseconds
list_sounds = ['None','Sound 1','Sound 2','Sound 3','Sound 4','Sound 5','Sound 6','Sound 7','Sound 8','Sound 9','Sound 10','Sound 11']

class PanZoomView(QtWidgets.QGraphicsView):
    """An interactive view that supports Pan and Zoom functions"""

    def __init__(self, scene):
        super().__init__(scene)
        # enable anti-aliasing
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        # enable drag and drop of the view
        self.setDragMode(self.ScrollHandDrag)

    def wheelEvent(self, event):
        """Overrides method in QGraphicsView in order to zoom it when mouse scroll occurs"""
        factor = math.pow(1.001, event.angleDelta().y())
        self.zoom_view(factor)

    @QtCore.pyqtSlot(int)
    def zoom_view(self, factor):
        """Updates the zoom factor of the view"""
        self.setTransformationAnchor(self.AnchorUnderMouse)
        super().scale(factor, factor)


class View(QtWidgets.QWidget):
    """An interactive view of the sound"""

    def __init__(self,the_sound):
        super().__init__()

        self.time_increment = 1

        # create components
        root_layout = QtWidgets.QVBoxLayout(self)
        self.scene = QtWidgets.QGraphicsScene()
        self.view = PanZoomView(self.scene)
        self.sound = the_sound
        self.time_entry = QtWidgets.QLineEdit()
        self.parameters_window1=["Ellipse","RMS"]


        toolbar = self.create_toolbar()

        # add components to the root_layout
        root_layout.addWidget(self.view)
        root_layout.addLayout(toolbar)

        # create and setup the timer
        self.timer = QtCore.QTimer(self)
        # self.timer.timeout.connect(self.advance)
        #root_layout.
        # show the window
        self.show()
    def sound1_chosen(self):
        self.chosen_sound="s1"
    def sound2_chosen(self):
        self.chosen_sound="s2"
    def create_toolbar(self):
        # create layout for time controls and entry
        toolbar = QtWidgets.QHBoxLayout()

        def add_button(text, slot):
            """adds a button to the hbox and connects the slot"""
            button = QtWidgets.QPushButton(text)
            button.clicked.connect(slot)
            toolbar.addWidget(button)

        # lambda function allows to pass extra arguments to slots
        # added space around '-' character to avoid different look and feel
        add_button('-', lambda: self.view.zoom_view(1/1.1))
        add_button('+', lambda: self.view.zoom_view(1.1))

        toolbar.addStretch()

        add_button('|>', self.playpause)

        toolbar.addStretch()

        def add_comboBox(sounds):
            """adds a comboBox to the hbox and connects the slot"""
            sounds_ComboBox = QtWidgets.QComboBox()

            for sound in sounds:
                sounds_ComboBox.addItem(sound)

            # comboBox.clicked.connect(slot)
            #for element in list_sounds:
            #sounds_ComboBox.currentTextChanged('Sound 1').connect(self.sound1_chosen)
            #sounds_ComboBox.currentTextChanged('Sound 2').connect(self.sound2_chosen) #def fonction 1 pour choisir son 1
            toolbar.addWidget(sounds_ComboBox)



        # labels
        lbl = QtWidgets.QLabel("Sounds")
        toolbar.addWidget(lbl)

        add_comboBox(list_sounds)

        toolbar.addStretch()




        # shortcuts and key bindings
        def add_shortcut(text, slot):
            """creates an application-wide key binding"""
            shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(text), self)
            shortcut.activated.connect(slot)

        add_shortcut('-', lambda: self.view.zoom_view(1/1.1))
        add_shortcut('+', lambda: self.view.zoom_view(1.1))
        add_shortcut(' ', self.playpause)
        add_shortcut('q', QtCore.QCoreApplication.instance().quit)

        return toolbar

    def fit_scene_in_view(self):
        self.view.fitInView(self.view.sceneRect(), QtCore.Qt.KeepAspectRatio)


    @QtCore.pyqtSlot()
    def change_time(self):
        """slot triggered when a new time is input in the text field"""
        # self.simulation.set_time(traffic.time_step(self.time_entry.text()))
        self.time_entry.clearFocus()
        self.update_traffic()

    @QtCore.pyqtSlot()
    def advance(self):
        """this slot computes the new time at each time out"""
        self.simulation.increment_time(self.time_increment)
        self.update_traffic()

    @QtCore.pyqtSlot(int)
    def set_time_increment(self, dt):
        """this slot updates the speed of the replay"""
        self.time_increment = dt
        self.speed_slider.setValue(dt)

    @QtCore.pyqtSlot()
    def playpause(self):
        """this slot toggles the replay using the timer as model"""
        #windows1

        #Ellipse=figures.Ellipse()
        #self.scene.addEllipse()


        if self.timer.isActive():
            self.timer.stop()
        else:
            self.sound.analyze()
            pygame.mixer.init()
            pygame.mixer.music.load(self.sound.filename)

            self.timer.timeout.connect(self.timer_update)

            pygame.mixer.music.play(0)
            self.timer.start(self.sound.analyse_parameters["frame_duration_ms"])




    def timer_update(self):
        if (pygame.mixer.music.get_busy()):
            self.scene.clear()
            qpen=QPen()
            qpen.setWidth(10)
            current_time = pygame.mixer.music.get_pos()
                # find closest frame in descriptors
            index = current_time // self.sound.analyse_parameters["frame_duration_ms"]
            index = round(min(index, self.sound.rms_frames[0].size - 1))
            rms = self.sound.rms_frames[0][index]
            spectral_centroid = self.sound.spectral_centroid_frames[0][index]

            spectral_flatness = self.sound.spectral_flatness_frames[0][index]

            self.scene.addEllipse(self.view.size().height() //2 ,self.view.size().width() //2,10*spectral_centroid,10*spectral_centroid,qpen,qbrush)
            self.fit_scene_in_view()


            #print(rms, spectral_flatness, spectral_centroid)
        else:
            self.timer.stop()