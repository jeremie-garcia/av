"""Defines different formes and their characteristics of reprepresented pictures"""

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QPainterPath, QPen, QColor, QLinearGradient, QRadialGradient
from PyQt5.QtCore import Qt, QRectF
import view


class Figure(QtWidgets.QGraphicsItem):
    def __init__(self, window1_parameters, the_view, the_scene):
        super().__init__()
        self.parameters = window1_parameters

        self.gradient = QLinearGradient()

        self.pen = QPen()
        self.brush = QBrush()
        self.color = []
        self.view = the_view
        self.scene = the_scene

        self.minor_axe = None
        self.major_axe = None
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
            raise NameError('Forme non définie')

    def SetToolsColor(self, recorded_frames):
        self.pen.setWidth(2)
        # set the color
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

        # set the color ratio
        if self.parameters["colorPara"] == "RMS":

            self.color[0] *= recorded_frames["rms"]
            self.color[1] *= recorded_frames["rms"]
            self.color[2] *= recorded_frames["rms"]
        elif self.parameters["colorPara"] == "Spectral centroid":
            self.color[0] *= recorded_frames["spectral_centroid"]
            self.color[1] *= recorded_frames["spectral_centroid"]
            self.color[2] *= recorded_frames["spectral_centroid"]
        else:
            self.color[0] *= recorded_frames["spectral_flatness"]
            self.color[1] *= recorded_frames["spectral_flatness"]
            self.color[2] *= recorded_frames["spectral_flatness"]

        # fix the color of the Tools
        self.gradient.setColorAt(0, QColor(self.color[0], self.color[1], self.color[2]))
        self.gradient.setColorAt(0.5, QColor(self.color[0], self.color[1], self.color[2], 175))
        self.gradient.setColorAt(1, QColor(self.color[0], self.color[1], self.color[2]))
        self.brush = QBrush(self.gradient)

        self.pen.setColor(QColor(self.color[0], self.color[1], self.color[2]))

    def update(self, recorded_frames):

        self.SetToolsColor(recorded_frames)

        # fix the horizontal value
        if self.parameters["horizPara"] == "RMS":
            self.major_axe = recorded_frames["rms"] * self.view.width()
        elif self.parameters["horizPara"] == "Spectral centroid":
            self.major_axe = recorded_frames["spectral_centroid"] * self.view.width()
        else:
            self.major_axe = recorded_frames["spectral_flatness"] * self.view.width()

            # fix the vertical value
        if self.parameters["verticPara"] == "RMS":
            self.minor_axe = recorded_frames["rms"] * self.view.height()
        elif self.parameters["verticPara"] == "Spectral centroid":
            self.minor_axe = recorded_frames["spectral_centroid"] * self.view.height()
        else:
            self.minor_axe = recorded_frames["spectral_flatness"] * self.view.height()

        # self.gradient.setCenter(self.view.height()//2, self.view.width()//2)
        # self.gradient.setRadius((self.minor_axe**2 + self.major_axe**2)**0.5)
        # self.gradient.setStart(0,0)
        # self.gradient.setFinalStop(self.view.height(), self.view.width())
        self.gradient.setStart((self.view.height() - self.minor_axe)//2, (self.view.width() - self.major_axe)//2)
        self.gradient.setFinalStop(self.view.height() - self.minor_axe//2, self.view.width() - self.major_axe//2)

        self.qrectf.setHeight(self.minor_axe)
        self.qrectf.setWidth(self.major_axe)

        self.item.setRect(self.qrectf)
        self.item.setBrush(self.brush)
        self.item.setPen(self.pen)

        self.scene.setSceneRect(self.qrectf)

