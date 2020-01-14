"""Module which defines a figure and its characteristics"""

from PyQt5 import QtWidgets
from PyQt5.QtGui import QBrush, QPen, QColor, QLinearGradient, QPolygonF
from PyQt5.QtCore import QRectF, QPointF


class Figure(QtWidgets.QGraphicsItem):
    def __init__(self, the_view, figure_index, color_dict):
        super().__init__()

        self.gradient = QLinearGradient()
        self.pen = QPen()
        self.brush = QBrush()
        self.color_dict = color_dict
        self.color = [0, 0, 0]
        self.color_basis = [0, 0, 0]
        self.view = the_view
        self.scene = the_view.scene
        self.parameters = self.view.figures_parameters[figure_index]
        self.size = [0, 0]
        self.qrectf = QRectF()
        self.item = None

    def Item_Init(self):
        if self.parameters[0] == "Rectangle":
            self.item = QtWidgets.QGraphicsRectItem()
            self.item.setRect(self.qrectf)
        elif self.parameters[0] == "Triangle":
            polygon = QPolygonF()
            polygon.append(QPointF(self.size[0] // 2, 0))
            polygon.append(QPointF(self.size[0], self.size[1]))
            polygon.append(QPointF(0, self.size[1]))
            self.item = QtWidgets.QGraphicsPolygonItem(polygon)
        else:
            self.item = QtWidgets.QGraphicsEllipseItem()
            self.item.setRect(self.qrectf)

        self.item.setBrush(self.brush)
        self.item.setPen(self.pen)
        self.scene.addItem(self.item)

    def update_gradient(self):
        # sets the starting and the final point of the gradient and its color
        self.gradient.setStart(0, 0)
        self.gradient.setFinalStop(self.size[0], self.size[1])
        self.gradient.setColorAt(0, QColor(self.color[0], self.color[1], self.color[2]))
        self.gradient.setColorAt(0.5, QColor(self.color[0], self.color[1], self.color[2], 150))
        self.gradient.setColorAt(1, QColor(self.color[0], self.color[1], self.color[2]))
        
        # updates brush
        self.brush = QBrush(self.gradient)

    def update_color(self, recorded_values):
        self.pen.setWidth(2)
        # sets color
        self.color_basis = self.color_dict[self.parameters[3]][:]

        # sets color ratio

        for i in range(len(self.color)):
            self.color[i] = self.color_basis[i] * recorded_values[self.parameters[4]]

        # fix the color of the Tool
        self.pen.setColor(QColor(self.color[0], self.color[1], self.color[2]))

    def update(self, size_coeff, recorded_values):

        # updates color and gradient
        self.update_color(recorded_values)
        self.update_gradient()

        # fix the horizontal value with 0.80 arbitrary chosen to provide saturation
        self.size[0] = size_coeff[0] * recorded_values[self.parameters[1]] * self.view.width() * 0.80
        # fix the vertical value
        self.size[1] = size_coeff[1] * recorded_values[self.parameters[2]] * self.view.height() * 0.80

        self.qrectf.setWidth(self.size[0])
        self.qrectf.setHeight(self.size[1])

        if self.parameters[0] == "Triangle":
            polygon = QPolygonF()
            polygon.append(QPointF(self.size[0] // 2, 0))
            polygon.append(QPointF(self.size[0], self.size[1]))
            polygon.append(QPointF(0, self.size[1]))
            self.item.setPolygon(polygon)
        else:
            self.item.setRect(self.qrectf)

        self.item.setBrush(self.brush)
        self.item.setPen(self.pen)

        self.scene.setSceneRect(self.qrectf)
