"""Defines different formes and their characteristics of reprepresented pictures"""

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QPaintDevice, QBrush, QPainterPath
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QRectF
import PyQt5.QtCore
import PyQt5


class Ellipse(QtWidgets.QGraphicsEllipseItem):
    def __init__(self):
        super().__init__()
        self.line_color = None  # doit être une couleur de Qt (ex: Qt.red)
        self.fill_color = None  # idem
        self.line_width = None
        self.semi_minor_axe = None
        self.semi_major_axe = None
        self.rect = QRectF()

        self.update_atributes()

    def update_atributes(self):
        self.line_color = Qt.blue  # à modifier en fonction du choix de l'utilisateur ou de l'analyse du son
        self.fill_color = Qt.white  # idem
        self.semi_minor_axe = 150  # idem
        self.semi_major_axe = 150  # idem
        self.rect = QRectF(0, 0, self.semi_major_axe, self.semi_minor_axe)
        self.setPen(QPen(self.line_color, self.line_width))
        self.setBrush(QBrush(self.fill_color, Qt.SolidPattern))

        self.setRect(self.rect)
        self.update()


class Rectangle(QtWidgets.QGraphicsRectItem):  #TODO classe parente : QtWidgets.QGraphicsRectItem
    def __init__(self):
        super().__init__()
        self.line_color = None
        self.fill_color = None
        self.line_width = None
        self.height = None
        self.width = None

        self.update_attributes()
        self.setGeometry()

    def update_atributes(self):
        self.line_color = Qt.blue
        self.fill_color = Qt.blue
        self.height = 100
        self.width = 100
        self.setRect(0, 0, self.height, self.width) # à valider
        self.setPen(QPen(self.line_color, self.line_width))
        self.setBrush(QBrush(self.fill_color, Qt.SolidPattern))

        self.update()


#QGraphicsItem plutot
class Triangle(QtWidgets.QGraphicsPolygonItem):  # TODO classe parente QWidget.QgraphicspolygonItem
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
