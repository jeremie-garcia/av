"""Sound visualization.
This module allows the visualization of a sound and its variations
on a scalable graphics view"""


from PyQt5 import QtWidgets, QtGui, QtCore
import figures
import pygame


class View(QtWidgets.QWidget):
    """An interactive view of the sound"""

    def __init__(self, the_sound):
        super().__init__()

        self.time_increment = 1

        # create components
        root_layout = QtWidgets.QVBoxLayout(self)
        self.scene = QtWidgets.QGraphicsScene()
        self.zoomview = QtWidgets.QGraphicsView(self.scene)
        self.sound = the_sound
        self.time_entry = QtWidgets.QLineEdit()
        self.color_dict = {"Red": [255, 0, 0], "Green": [0, 255, 0], "Blue": [0, 0, 255], "Yellow": [255, 255, 0],
                           "Grey": [255, 255, 255]}
        self.forms = ["None", "Ellipse", "Rectangle"]
        self.sound_parameters = ["RMS", "Spectral centroid", "Spectral flatness"]
        self.isSoundPlayed = False
        self.isSoundChanged = False

        self.figures_status = [True, True, True, True]

        self.figures_parameters = [["Ellipse",  "RMS", "RMS", "Red", "RMS"],
                                   ["Ellipse", "Spectral flatness", "Spectral flatness", "Blue", "RMS"],
                                   ["Ellipse", "Spectral centroid", "Spectral centroid", "Green", "RMS"],
                                   ["Ellipse", "RMS", "Spectral centroid", "Yellow", "RMS"]]
        # form, horizontalPara, verticalPara, color, colorPara

        self.center_presetting = [[(1 / 2, 1 / 2)],
                                  [(1 / 4, 1 / 2), (3 / 4, 1 / 2)],
                                  [(1 / 4, 1 / 4), (3 / 4, 1 / 4), (1 / 2, 3 / 4)],
                                  [(1 / 4, 1 / 4), (3 / 4, 1 / 4), (1 / 4, 3 / 4), (3 / 4, 3 / 4)]]
        self.size_presetting = [[(1, 1)],
                                [(1 / 2, 1), (1 / 2, 1)],
                                [(1 / 2, 1 / 2), (1 / 2, 1 / 2), (1 / 2, 1 / 2)],
                                [(1 / 2, 1 / 2), (1 / 2, 1 / 2), (1 / 2, 1 / 2), (1 / 2, 1 / 2)]]

        self.figures = [None, None, None, None]

        toolbar = self.create_toolbar()

        # add components to the root_layout
        root_layout.addWidget(self.zoomview)
        root_layout.addLayout(toolbar)

        # create and setup the timer
        self.timer = QtCore.QTimer(self)

        self.update_scene_size()

    def update_scene_size(self):
        # fix scene size to the view size
        self.zoomview.setSceneRect(0, 0, self.zoomview.width(), self.zoomview.height())

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
        add_button('-', lambda: self.zoomview.scale(1/1.1, 1/1.1))
        add_button('+', lambda: self.zoomview.scale(1.1, 1.1))

        toolbar.addStretch()

        add_button('|>', self.playpause)

        toolbar.addStretch()

        # shortcuts and key bindings
        def add_shortcut(text, slot):
            """creates an application-wide key binding"""
            shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(text), self)
            shortcut.activated.connect(slot)

        add_shortcut('-', lambda: self.zoomview.scale(1/1.1, 1/1.1))
        add_shortcut('+', lambda: self.zoomview.scale(1.1, 1.1))
        add_shortcut(' ', self.playpause)
        add_shortcut('q', QtCore.QCoreApplication.instance().quit)

        return toolbar

    def fit_scene_in_view(self):
        self.zoomview.fitInView(self.zoomview.sceneRect(), QtCore.Qt.KeepAspectRatio)

    def figures_constructor(self):
        self.scene.clear()
        for index in range(len(self.figures_status)):
            if self.figures_status[index]:
                self.figures[index] = figures.Figure(self, index, self.color_dict)
                self.figures[index].Item_Init()
            else:
                self.figures[index] = None

    def update_figures_in_view(self, recorded_values):
        """updates center and size"""
        nb_figures = sum(self.figures_status)
        compteur = 0
        for index in range(len(self.figures_status)):
            if self.figures_status[index]:
                # color, size update
                coeff_size = self.size_presetting[nb_figures-1][compteur]
                self.figures[index].update(coeff_size, recorded_values)
                # center update
                coeff_center = self.center_presetting[nb_figures-1][compteur]
                x_center = coeff_center[0] * self.zoomview.width() - self.figures[index].size[0]//2
                y_center = coeff_center[1] * self.zoomview.height() - self.figures[index].size[1]//2
                self.figures[index].item.setPos(x_center, y_center)
                compteur += 1

    @QtCore.pyqtSlot()
    def playpause(self):
        """this slot toggles the replay using the timer as model"""
        # windows1

        if self.timer.isActive():
            self.timer.stop()
            pygame.mixer.music.pause()           # pause and play again after <-- to set
        else:
            if self.isSoundPlayed:
                pygame.mixer.music.unpause()
                self.timer.start(self.sound.analyse_parameters["frame_duration_ms"])
            else:
                self.isSoundPlayed = True
                self.sound.analyze()
                self.sound.normalize_figures()
                self.figures_constructor()

                pygame.mixer.init()

                pygame.mixer.music.load(self.sound.filename)

                self.timer.timeout.connect(self.timer_update)

                pygame.mixer.music.play(0)
                self.timer.start(self.sound.analyse_parameters["frame_duration_ms"])

    def timer_update(self):
        self.update_scene_size()

        if pygame.mixer.music.get_busy() and not self.isSoundChanged:
            current_time = pygame.mixer.music.get_pos()

            index = current_time // self.sound.analyse_parameters["frame_duration_ms"]
            index = round(min(index, self.sound.rms_frames[0].size - 1))
            rms = self.sound.rms_frames[0][index]
            spectral_centroid = self.sound.spectral_centroid_frames[0][index]
            spectral_flatness = self.sound.spectral_flatness_frames[0][index]
            recorded_values = {"RMS": float(rms), "Spectral centroid": float(spectral_centroid),
                               "Spectral flatness": float(spectral_flatness)}
            self.update_figures_in_view(recorded_values)

        elif pygame.mixer.music.get_busy() and self.isSoundChanged:
            self.timer.stop()
            pygame.mixer.music.stop()
            self.isSoundPlayed = False
            self.isSoundChanged = False
            self.scene.clear()

        else:
            self.timer.stop()
            pygame.mixer.music.stop()
            self.isSoundPlayed = False
            self.scene.clear()
