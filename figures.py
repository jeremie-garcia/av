"""Defines different formes and their characteristics of reprepresented pictures"""

from PyQt5 import QtWidgets
from PyQt5.QtGui import QBrush, QPen, QColor, QLinearGradient
from PyQt5.QtCore import QRectF


class Figure(QtWidgets.QGraphicsItem):
    def __init__(self, the_view, window_parameters):
        super().__init__()
        self.parameters = window_parameters
        self.gradient = QLinearGradient()
        self.pen = QPen()
        self.brush = QBrush()
        self.color = []
        self.view = the_view
        self.scene = the_view.scene

        self.vertical_size = 100
        self.horizontal_size = 100
        self.qrectf = QRectF()
        self.item = None

    def Item_Init(self):
        if self.parameters["form"] == "Rectangle":
            self.item = QtWidgets.QGraphicsRectItem()
            self.item.setRect(self.qrectf)
            self.item.setBrush(self.brush)
            self.item.setPen(self.pen)
            self.scene.addItem(self.item)

        if self.parameters["form"] == "Ellipse":
            self.item = QtWidgets.QGraphicsEllipseItem()
            self.item.setRect(self.qrectf)
            self.item.setBrush(self.brush)
            self.item.setPen(self.pen)
            self.scene.addItem(self.item)

        else:
            print('Forme non définie')

    def update_gradient(self):
        # sets the starting and the final point of the gradient and its color
        self.gradient.setStart(0, 0)
        self.gradient.setFinalStop(self.horizontal_size, self.vertical_size)
        self.gradient.setColorAt(0, QColor(self.color[0], self.color[1], self.color[2]))
        self.gradient.setColorAt(0.5, QColor(self.color[0], self.color[1], self.color[2], 150))
        self.gradient.setColorAt(1, QColor(self.color[0], self.color[1], self.color[2]))
        
        # updates brush
        self.brush = QBrush(self.gradient)

    def SetToolsColor(self, recorded_frames):
        self.pen.setWidth(2)
        # sets color
        if self.parameters["color"] == "Red":
            self.color = [255, 0, 0]
        elif self.parameters["color"] == "Green":
            self.color = [0, 255, 0]
        elif self.parameters["color"] == "Blue":
            self.color = [0, 0, 255]
        elif self.parameters["color"] == "Yellow":
            self.color = [255, 255, 0]
        elif self.parameters["color"] == "Grey":
            self.color = [255, 255, 255]
        else:
            self.color = [255, 0, 255]

        # sets color ratio
        if self.parameters["colorPara"] == "RMS":

            self.color[0] *= recorded_frames["RMS"]
            self.color[1] *= recorded_frames["RMS"]
            self.color[2] *= recorded_frames["RMS"]
        elif self.parameters["colorPara"] == "Spectral centroid":
            self.color[0] *= recorded_frames["Spectral centroid"]
            self.color[1] *= recorded_frames["Spectral centroid"]
            self.color[2] *= recorded_frames["Spectral centroid"]
        else:
            self.color[0] *= recorded_frames["Spectral flatness"]
            self.color[1] *= recorded_frames["Spectral flatness"]
            self.color[2] *= recorded_frames["Spectral flatness"]

        # fix the color of the Tool
        self.pen.setColor(QColor(self.color[0], self.color[1], self.color[2]))

    def update(self, recorded_frames):
        nb_figure = sum(self.view.figures_list)

        if nb_figure == 1 or nb_figure == 2:
            # fix the horizontal value
            if self.parameters["horizPara"] == "RMS":
                self.horizontal_size = recorded_frames["RMS"] * self.view.width() * 0.80 // nb_figure
            elif self.parameters["horizPara"] == "Spectral centroid":
                self.horizontal_size = recorded_frames["Spectral centroid"] * self.view.width() * 0.80 // nb_figure
            else:
                self.horizontal_size = recorded_frames["Spectral flatness"] * self.view.width() * 0.80 // nb_figure

            # fix the vertical value
            if self.parameters["verticPara"] == "RMS":
                self.vertical_size = recorded_frames["RMS"] * self.view.height() * 0.80
            elif self.parameters["verticPara"] == "Spectral centroid":
                self.vertical_size = recorded_frames["Spectral centroid"] * self.view.height() * 0.80
            else:
                self.vertical_size = recorded_frames["Spectral flatness"] * self.view.height() * 0.80

        elif nb_figure == 3 or nb_figure == 4:
            if self.parameters["horizPara"] == "RMS":
                self.horizontal_size = recorded_frames["RMS"] * self.view.width() * 0.80 // 2
            elif self.parameters["horizPara"] == "Spectral centroid":
                self.horizontal_size = recorded_frames["Spectral centroid"] * self.view.width() * 0.80 // 2
            else:
                self.horizontal_size = recorded_frames["Spectral flatness"] * self.view.width() * 0.80 // 2

            # fix the vertical value
            if self.parameters["verticPara"] == "RMS":
                self.vertical_size = recorded_frames["RMS"] * self.view.height() * 0.80 // 2
            elif self.parameters["verticPara"] == "Spectral centroid":
                self.vertical_size = recorded_frames["Spectral centroid"] * self.view.height() * 0.80 // 2
            else:
                self.vertical_size = recorded_frames["Spectral flatness"] * self.view.height() * 0.80 // 2

        # updates color and gradient
        self.SetToolsColor(recorded_frames)
        self.update_gradient()

        self.qrectf.setHeight(self.vertical_size)
        self.qrectf.setWidth(self.horizontal_size)

        self.item.setRect(self.qrectf)
        self.item.setBrush(self.brush)
        self.item.setPen(self.pen)

        self.scene.setSceneRect(self.qrectf)
