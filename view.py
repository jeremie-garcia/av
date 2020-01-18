"""Sound visualization.
This module allows the visualization of a sound and its variations
on a scalable graphics view"""

from PyQt5 import QtWidgets, QtGui, QtCore
import figures
import pygame


class View(QtWidgets.QWidget):
    """An interactive view of the sound
    this object holds a scene (QGraphicsScene) with figures"""

    def __init__(self, the_sound):
        super().__init__()

        # create components
        root_layout = QtWidgets.QVBoxLayout(self)
        self.scene = QtWidgets.QGraphicsScene()
        self.zoomview = QtWidgets.QGraphicsView(self.scene)
        self.sound = the_sound
        self.time_entry = QtWidgets.QLineEdit()
        self.color_dict = {"Red": [255, 0, 0], "Green": [0, 255, 0], "Blue": [0, 0, 255], "Yellow": [255, 255, 0],
                           "Grey": [255, 255, 255]}
        self.forms = ["None", "Ellipse", "Rectangle", "Triangle"]
        self.sound_parameters = ["RMS", "Spectral centroid", "Spectral flatness"]

        self.isSoundPlayed = False
        self.isSoundChanged = False
        self.isFormChanged = False

        # form, horizontalParameter, verticalParameter, color, colorParameter
        self.figures_parameters = [["Ellipse",  "RMS", "RMS", "Red", "RMS"],
                                   ["Ellipse", "Spectral flatness", "Spectral flatness", "Blue", "RMS"],
                                   ["Ellipse", "Spectral centroid", "Spectral centroid", "Green", "RMS"],
                                   ["Ellipse", "RMS", "Spectral centroid", "Yellow", "RMS"]]

        # define size and center of figures depending on the number of figures
        self.center_presetting = [[(1 / 2, 1 / 2)],
                                  [(1 / 4, 1 / 2), (3 / 4, 1 / 2)],
                                  [(1 / 4, 1 / 4), (3 / 4, 1 / 4), (1 / 2, 3 / 4)],
                                  [(1 / 4, 1 / 4), (3 / 4, 1 / 4), (1 / 4, 3 / 4), (3 / 4, 3 / 4)]]
        self.size_presetting = [[(1, 1)],
                                [(1 / 2, 1), (1 / 2, 1)],
                                [(1 / 2, 1 / 2), (1 / 2, 1 / 2), (1 / 2, 1 / 2)],
                                [(1 / 2, 1 / 2), (1 / 2, 1 / 2), (1 / 2, 1 / 2), (1 / 2, 1 / 2)]]

        # create figures
        self.figures_status = [True, True, True, True]
        self.figures = [None, None, None, None]
        self.figures_constructor()

        toolbar = self.create_toolbar()

        # add components to the root_layout
        root_layout.addWidget(self.zoomview)
        root_layout.addLayout(toolbar)

        # creates and setup the timer
        self.timer = QtCore.QTimer(self)

        self.update_scene_size()

    def update_scene_size(self):
        """fixes scene size to the view size"""
        self.zoomview.setSceneRect(0, 0, self.zoomview.width(), self.zoomview.height())

    def fit_scene_in_view(self):
        """fits the scene in the view"""
        self.zoomview.fitInView(self.zoomview.sceneRect(), QtCore.Qt.KeepAspectRatio)

    def create_toolbar(self):
        """creates layout for time controls and entry"""
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

    def figures_constructor(self):
        """creates figures based on the status of figures"""
        self.scene.clear()
        for index in range(len(self.figures_status)):
            if self.figures_status[index]:
                self.figures[index] = figures.Figure(self, index, self.color_dict)
                self.figures[index].item_init()
            else:
                self.figures[index] = None

    def update_figures_in_view(self, recorded_values):
        """updates center and size in the scene based on presetting lists"""
        nb_figures = sum(self.figures_status)
        index_list = 0
        for index in range(len(self.figures_status)):
            if self.figures_status[index]:

                # color, size update
                coeff_size = self.size_presetting[nb_figures-1][index_list]
                self.figures[index].update(coeff_size, recorded_values)

                # center update
                coeff_center = self.center_presetting[nb_figures-1][index_list]
                x_center = coeff_center[0] * self.zoomview.width() - self.figures[index].size[0]//2
                y_center = coeff_center[1] * self.zoomview.height() - self.figures[index].size[1]//2
                self.figures[index].item.setPos(x_center, y_center)
                index_list += 1

    @QtCore.pyqtSlot()
    def playpause(self):
        """this slot toggles the replay using the timer as model"""

        if self.timer.isActive():
            self.timer.stop()
            pygame.mixer.music.pause()

        # to set pause and play again after
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
        """manages timer, depend on music played or not, figures changed or not, sound changed or not
        update figures parameters based on the analyzed sound"""
        self.update_scene_size()

        if pygame.mixer.music.get_busy() and not (self.isSoundChanged or self.isFormChanged):
            current_time = pygame.mixer.music.get_pos()

            index = current_time // self.sound.analyse_parameters["frame_duration_ms"]
            index = round(min(index, self.sound.rms_frames[0].size - 1))
            recorded_values = {"RMS": float(self.sound.rms_frames[0][index]),
                               "Spectral centroid": float(self.sound.spectral_centroid_frames[0][index]),
                               "Spectral flatness": float(self.sound.spectral_flatness_frames[0][index])}
            self.update_figures_in_view(recorded_values)

        elif pygame.mixer.music.get_busy() and (self.isSoundChanged or self.isFormChanged):
            self.timer.stop()
            pygame.mixer.music.stop()
            self.isSoundPlayed = False
            self.isSoundChanged = False
            self.isFormChanged = False
            self.scene.clear()

        else:
            self.timer.stop()
            pygame.mixer.music.stop()
            self.isSoundPlayed = False
            self.scene.clear()
