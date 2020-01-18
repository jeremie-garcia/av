"""Main module for the code"""


from PyQt5 import QtCore, QtWidgets
import view, sound_analyzer, selector

if __name__ == "__main__":

    # Initialize Qt
    app = QtWidgets.QApplication([])

    # create the view and the sound
    the_sound = sound_analyzer.Sound()
    the_view = view.View(the_sound)
    the_view.fit_scene_in_view()
    the_view.setStyleSheet("background-color:lightgray;")

    # create the selector
    selec = selector.Selector(the_view)

    # create a QDockWidget for selector
    selec_dock = QtWidgets.QDockWidget()
    selec_dock.setWidget(selec)

    # create the QMainWindow and add widgets
    win = QtWidgets.QMainWindow()
    win.setWindowTitle("Sound Visualizer")
    win.setCentralWidget(the_view)
    win.addDockWidget(QtCore.Qt.DockWidgetArea(1), selec_dock)
    win.showMaximized()

    app.exec_()