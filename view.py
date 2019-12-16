"""Sound visualization.

This module allows the visualization of a sound and its variations
on a scalable graphics view"""

import math

from PyQt5 import QtWidgets, QtGui, QtCore
import pygame
import figures


# constants
WIDTH = 800  # Initial window width (pixels)
HEIGHT = 450  # Initial window height (pixels)
ANIMATION_DELAY = 50  # milliseconds
list_sounds = ['None', 'Sound 1', 'Sound 2', 'Sound 3', 'Sound 4', 'Sound 5',
               'Sound 6', 'Sound 7', 'Sound 8', 'Sound 9', 'Sound 10', 'Sound 11']


class PanZoomView(QtWidgets.QGraphicsView):
    """An interactive view that supports Pan and Zoom functions"""

    def __init__(self, scene):
        super().__init__(scene)
        # enable anti-aliasing
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        # enable drag and drop of the view
        # self.setDragMode(self.ScrollHandDrag)

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

    def __init__(self, the_sound):
        super().__init__()

        self.time_increment = 1

        # create components
        root_layout = QtWidgets.QVBoxLayout(self)
        self.scene = QtWidgets.QGraphicsScene()
        self.view = PanZoomView(self.scene)
        self.sound = the_sound
        self.time_entry = QtWidgets.QLineEdit()
        self.view.parameters_window1 = {"form": "Ellipse", "horizPara": "RMS",
                                        "verticPara": "RMS", "color": "Red", "colorPara": "RMS"}
        self.view.parameters_window2 = {"form": None, "horizPara": None, "verticPara": None,
                                        "color": None, "colorPara": None}
        self.view.parameters_window3 = {"form": None, "horizPara": None, "verticPara": None,
                                        "color": None, "colorPara": None}
        self.view.parameters_window4 = {"form": None, "horizPara": None, "verticPara": None,
                                        "color": None, "colorPara": None}

        toolbar = self.create_toolbar()

        # add components to the root_layout
        root_layout.addWidget(self.view)
        root_layout.addLayout(toolbar)

        # create and setup the timer
        self.timer = QtCore.QTimer(self)
        # self.timer.timeout.connect(self.advance)
        # root_layout.
        # show the window
        self.show()

    # connection comboBox chosen Sound
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

            toolbar.addWidget(sounds_ComboBox)
            # return sounds_ComboBox.currentText()

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
    def playpause(self):
        """this slot toggles the replay using the timer as model"""
        # windows1

        # Ellipse=figures.Ellipse()
        # self.scene.addEllipse()

        if self.timer.isActive():
            self.timer.stop()
            pygame.mixer.music.stop()           # pause and play again after <-- to set
        else:
                self.sound.analyze()
                self.sound.normalize()
                figure=figures.Figure(self.view.parameters_window1,self.view,self.scene)
                pygame.mixer.init()

                pygame.mixer.music.load(self.sound.filename)

                self.timer.timeout.connect(self.timer_update)

                pygame.mixer.music.play(0)
                self.timer.start(self.sound.analyse_parameters["frame_duration_ms"])

    def timer_update(self):
        if pygame.mixer.music.get_busy():
            self.scene.clear()



            current_time = pygame.mixer.music.get_pos()

            index = current_time // self.sound.analyse_parameters["frame_duration_ms"]
            index = round(min(index, self.sound.rms_frames[0].size - 1))
            rms = self.sound.rms_frames[0][index]
            spectral_centroid = self.sound.spectral_centroid_frames[0][index]
            spectral_flatness = self.sound.spectral_flatness_frames[0][index]
            recorded_values = {"rms": float(rms) , "spectral_centroid": float(spectral_centroid),
                             "spectral_flatness": float(spectral_flatness)}

            figure.update(recorded_values)

            # self.scene.addEllipse(self.view.size().height() //2, self.view.size().width()//2,
            #                       10*spectral_centroid, 10*spectral_centroid, qpen, qpaint)

            # print(rms, spectral_flatness, spectral_centroid)
        else:
            self.timer.stop()
            pygame.mixer.music.stop()

