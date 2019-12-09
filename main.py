import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import librosa
import view, sound_analizer, figures
import selector_test

if __name__ == "__main__":

    # Initialize Qt
    app = QtWidgets.QApplication([])

    # create the radar view and the time navigation interface
    the_view = view.View()
    the_view.move(10, 10)

    # create the inspector
    selec = selector_test.Selector(the_view)

    # create a QDockWidget for the inspector
    selec_dock = QtWidgets.QDockWidget()
    selec_dock.setWidget(selec)

    # create the QMainWindow and add both widgets
    win = QtWidgets.QMainWindow()
    win.setWindowTitle("Sound Visualisator")
    win.setCentralWidget(the_view)
    win.addDockWidget(QtCore.Qt.DockWidgetArea(1), selec_dock)
    # win.resize(1000, 600)
    # win.show()
    win.showMaximized()

    # create the second view
    # second_view = radarview.PanZoomView(main_window.scene)
    # second_view.scale(0.1, -0.1)
    # second_view.show()
    # second_view.move(300, 300)

    # enter the main loop
    app.exec_()
