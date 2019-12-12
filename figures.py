"""Defines different formes and their characteristics of reprepresented pictures"""

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QPaintDevice, QBrush, QPainterPath, QPen, QColor
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











"""class de test - ben"""

class figure_test():
    def __init__(self,window1_parameters):
        self.parameters=window1_parameters
        self.drawingToolsWindow1={"pen" : QPen(),"brush" : QBrush()}
        self.color=[]

            
        
    def draw(self,view,scene,recorded_frames):
        if self.parameters["form"]=="Rectangle":
            self.SetToolsColor(recorded_frames)
            self.Rectangle(view,scene,recorded_frames)

        else :
            self.SetToolsColor(recorded_frames)
            self.Ellipse(view,scene,recorded_frames)


            

    def SetToolsColor(self,recorded_frames):
        self.drawingToolsWindow1["pen"].setWidth(20)
        self.drawingToolsWindow1["brush"].setStyle(1)      #the number changes the type of background
        "set the color "
        if self.parameters["color"]=="Red":
            self.color=[255,0,0]
        elif self.parameters["color"]=="Green":
            self.color=[0,255,0]
        elif self.parameters["color"]=="Blue":
            self.color=[0,0,255]
        elif self.parameters["color"]=="Yellow":
            self.color=[255,255,0]
        elif self.parameters["color"]=="Grey":
            self.color=[255,255,255]
        else: self.color=[255,0,255]
        
        
        "set the color ratio"
        if self.parameters["colorPara"]== "RMS":

            self.color[0] *=recorded_frames["rms"]
            self.color[1] *= recorded_frames["rms"]
            self.color[2] *= recorded_frames["rms"]
        elif self.parameters["colorPara"]== "Spectral centroid":
            self.color[0]*=recorded_frames["spectral_centroid"]
            self.color[1] *= recorded_frames["spectral_centroid"]
            self.color[2] *= recorded_frames["spectral_centroid"]
        else:
            self.color[0]*=recorded_frames["spectral_flatness"]
            self.color[1] *= recorded_frames["spectral_flatness"]
            self.color[2] *= recorded_frames["spectral_flatness"]

        "fix the color of the Tools"

        self.drawingToolsWindow1["brush"].setColor(QColor(self.color[0],self.color[1],self.color[2]))
        self.drawingToolsWindow1["pen"].setColor(QColor(self.color[0], self.color[1], self.color[2]))


            
            
    
    def Rectangle(self, view, scene, recorded_frames):

        "fix the horiz value"

        if self.parameters["horizPara"] == "RMS":
            self.horiz_value = recorded_frames["rms"]* view.width()
        elif self.parameters["horizPara"] == "Spectral centroid":
            self.horiz_value = recorded_frames["spectral_centroid"] * view.width()
        else:
            self.horiz_value = recorded_frames["spectral_flatness"] * view.width()

        "fix the vertic value"
        if self.parameters["verticPara"]== "RMS":
            self.vertic_value=recorded_frames["rms"]* view.height()
        elif self.parameters["verticPara"]== "Spectral centroid":
            self.vertic_value=recorded_frames["spectral_centroid"] * view.height()
        else:
            self.vertic_value=recorded_frames["spectral_flatness"] * view.height()


        scene.addRect(view.width()//2, view.height()//2 , self.horiz_value,self.vertic_value,self.drawingToolsWindow1["pen"], self.drawingToolsWindow1["brush"])


    def Ellipse(self,view, scene, recorded_frames):

        "fix the horiz value"

        if self.parameters["horizPara"] == "RMS":
            self.horiz_value = recorded_frames["rms"] * view.width()
        elif self.parameters["horizPara"] == "spectral_centroid":
            self.horiz_value = recorded_frames["Spectral centroid"] * view.width()
        else:
            self.horiz_value = recorded_frames["spectral_flatness"] * view.width()

        "fix the vertic value"
        if self.parameters["verticPara"] == "RMS":
            self.vertic_value = recorded_frames["rms"] * view.height()
        elif self.parameters["verticPara"] == "Spectral centroid":
            self.vertic_value = recorded_frames["spectral_centroid"] * view.height()
        else:
            self.vertic_value = recorded_frames["spectral_flatness"] * view.height()

        #scene.setSceneRect(0,0,view.width(),view.height())
        scene.addEllipse(view.width()//2, view.height()//2, self.horiz_value, self.vertic_value,self.drawingToolsWindow1["pen"], self.drawingToolsWindow1["brush"])

        #fix the center shifting