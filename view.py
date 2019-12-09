"""Sound visualization.

This module allows the visualization of a sound and its variations
on a scalable graphics view"""

import math

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPen, QBrush, QColor

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

    def __init__(self):
        super().__init__()

        self.time_increment = 1

        # create components
        root_layout = QtWidgets.QVBoxLayout(self)
        self.scene = QtWidgets.QGraphicsScene()
        self.view = PanZoomView(self.scene)
        self.time_entry = QtWidgets.QLineEdit()
        toolbar = self.create_toolbar()

        # add components to the root_layout
        root_layout.addWidget(self.view)
        root_layout.addLayout(toolbar)

        # create and setup the timer
        self.timer = QtCore.QTimer(self)
        # self.timer.timeout.connect(self.advance)

        # show the window
        self.show()

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
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(ANIMATION_DELAY)
