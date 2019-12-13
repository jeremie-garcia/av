"""Defines different formes and their characteristics of reprepresented pictures"""

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QPainterPath, QPen, QColor
from PyQt5.QtCore import Qt, QRectF


# QGraphicsItem plutot
class Triangle(QtWidgets.QGraphicsPolygonItem):  # TODO a mettre dans la classe figure
    def __init__(self):
        super().__init__()
        self.line_color = None
        self.fill_color = None
        self.line_width = None
        self.first_side = None  # length of the first side of the triangle
        self.second_side = None  # length of the second side of the triangle

        self.set_atributes()

        self.setGeometry()

    def update_atributes(self):
        # Penser à utilser QPaninterPath.currentPosition() pour le calcul des positions des lignes du tiangle
        self.line_color = Qt.green
        self.fill_color = Qt.green

        self.setPen(QPen(self.line_color, self.line_width))
        self.setBrush(QBrush(self.fill_color, Qt.SolidPattern))

    def paintEvent(self, event):
        qp = QPainter()
        path = QPainterPath()
        path.moveTo(10, 25)  # à confirmer
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(self.line_color)
        qp.setBrush(QBrush(self.fill_color, Qt.SolidPattern))
        path.lineTo(160, 400)
        path.lineTo(350, 100)
        path.lineTo(10, 25)
        qp.drawPath(path)
        qp.end()


class Figure(QtWidgets.QGraphicsItem):
    def __init__(self, window1_parameters):
        print('init')
        super().__init__()
        self.parameters = window1_parameters
        self.drawingToolsWindow1 = {"pen": QPen(), "brush": QBrush()}
        self.color = []

        self.minor_axe = None
        self.major_axe = None
        self.qrectf = QRectF()

    def draw(self, view, scene, recorded_frames):
        print('draw')
        if self.parameters["form"] == "Rectangle":
            self.SetToolsColor(recorded_frames)
            self.Rectangle(view, scene, recorded_frames)

        else:
            self.SetToolsColor(recorded_frames)
            self.Ellipse(view, scene, recorded_frames)

    def SetToolsColor(self, recorded_frames):
        self.drawingToolsWindow1["pen"].setWidth(20)
        self.drawingToolsWindow1["brush"].setStyle(1)      # the number changes the type of background
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

        "fix the color of the Tools"

        self.drawingToolsWindow1["brush"].setColor(QColor(self.color[0], self.color[1], self.color[2]))
        self.drawingToolsWindow1["pen"].setColor(QColor(self.color[0], self.color[1], self.color[2]))

    def Rectangle(self, view, scene, recorded_frames):

        # fix the horiz value
        if self.parameters["horizPara"] == "RMS":
            self.major_axe = recorded_frames["rms"] * view.width()
        elif self.parameters["horizPara"] == "Spectral centroid":
            self.major_axe = recorded_frames["spectral_centroid"] * view.width()
        else:
            self.major_axe = recorded_frames["spectral_flatness"] * view.width()

        # fix the vertic value
        if self.parameters["verticPara"] == "RMS":
            self.minor_axe = recorded_frames["rms"] * view.height()
        elif self.parameters["verticPara"] == "Spectral centroid":
            self.minor_axe = recorded_frames["spectral_centroid"] * view.height()
        else:
            self.minor_axe = recorded_frames["spectral_flatness"] * view.height()

        self.qrectf = QRectF(view.width()//2, view.height()//2, self.major_axe, self.minor_axe)
        # self.rect = QtWidgets.QGraphicsRectItem(self.qrectf)
        # scene.addItem(self.qretf)
        scene.addRect(self.qrectf, self.drawingToolsWindow1["pen"], self.drawingToolsWindow1["brush"])

    def Ellipse(self, view, scene, recorded_frames):

        # fix the horiz value
        if self.parameters["horizPara"] == "RMS":
            self.major_axe = recorded_frames["rms"] * view.width()
        elif self.parameters["horizPara"] == "spectral_centroid":
            self.major_axe = recorded_frames["Spectral centroid"] * view.width()
        else:
            self.major_axe = recorded_frames["spectral_flatness"] * view.width()

        # fix the vertic value
        if self.parameters["verticPara"] == "RMS":
            self.minor_axe = recorded_frames["rms"] * view.height()
        elif self.parameters["verticPara"] == "Spectral centroid":
            self.minor_axe = recorded_frames["spectral_centroid"] * view.height()
        else:
            self.minor_axe = recorded_frames["spectral_flatness"] * view.height()

        self.qrectf = QRectF(view.width() // 2, view.height() // 2, self.major_axe, self.minor_axe)
        scene.addEllipse(self.qrectf, self.drawingToolsWindow1["pen"], self.drawingToolsWindow1["brush"])

        # scene.setSceneRect(0,0,view.width(),view.height())
        scene.addEllipse(view.width() // 2, view.height() // 2, self.major_axe, self.minor_axe,
                         self.drawingToolsWindow1["pen"], self.drawingToolsWindow1["brush"])
