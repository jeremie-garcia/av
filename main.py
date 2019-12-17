import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import view, sound_analyzer # figures
import selector

if __name__ == "__main__":

    # Initialize Qt
    app = QtWidgets.QApplication([])

    # create the radar view and the time navigation interface
    the_sound = sound_analyzer.Sound()
    the_view = view.View(the_sound)
    #the_view.fit_scene_in_view()
    #the_view.move(10, 10)

    #the_sound.change(the_view.chosen_sound)
    # create the inspector
    selec = selector.Selector(the_view.view)

    # create a QDockWidget for the inspector
    selec_dock = QtWidgets.QDockWidget()
    selec_dock.setWidget(selec)


    # create the QMainWindow and add both widgets
    win = QtWidgets.QMainWindow()
    win.setWindowTitle("Sound Visualiser")
    win.setCentralWidget(the_view)
    win.addDockWidget(QtCore.Qt.DockWidgetArea(1), selec_dock)
    win.showMaximized()

    app.exec_()
