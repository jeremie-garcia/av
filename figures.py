"""Defines different formes and their characteristics of reprepresented pictures"""

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QPaintDevice, QBrush, QPainterPath
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import PyQt5


class Ellipse(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.line_color = None  # doit être une couleur de Qt (ex: Qt.red)
        self.fill_color = None  # idem
        self.line_width = None
        self.semi_minor_axe = None
        self.semi_major_axe = None

        self.set_atributes()

        self.setGeometry(300, 300, 300, 300)
        self.show()

    def set_atributes(self):
        self.line_color = Qt.red  # à modifier en fonction du choix de l'utilisateur ou de l'analyse du son
        self.fill_color = Qt.red
        self.semi_minor_axe = 100  # idem
        self.semi_major_axe = 100  # idem

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(self.line_color)
        qp.setBrush(QBrush(self.fill_color, Qt.SolidPattern))  # J'ai rajouté le remplissage du cercle
        qp.drawArc(20, 20, self.semi_minor_axe, self.semi_major_axe, 0, 5700)
        qp.end()


class Rectangle(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.line_color = None
        self.fill_color = None
        self.line_width = None
        self.height = None
        self.width = None

        self.set_atributes()

        self.setGeometry()

    def set_atributes(self):
        self.line_color = Qt.blue
        self.fill_color = Qt.blue
        self.height = 100
        self.width = 100

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(self.line_color)
        qp.setBrush(QBrush(self.fill_color, Qt.SolidPattern))
        qp.drawRect(320, 20, self.width, self.height)
        qp.end()


#QGraphicsItem plutot
class Triangle(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.line_color = None
        self.fill_color = None
        self.line_width = None
        self.first_side = None  # length of the first side of the triangle
        self.second_side = None  # length of the second side of the triangle

        self.set_atributes()

        self.setGeometry()

    def set_atributes(self):
        # Penser à utilser QPaninterPath.currentPosition() pour le calcul des positions des lignes du tiangle
        self.line_color = Qt.green
        self.fill_color = Qt.green

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
