from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListView

from selector_test_ui import Ui_Form

class Selector(QWidget):
    """ Widget displaying selection parameters"""

    def __init__(self, the_view):
        super(Selector, self).__init__()

        self.view = the_view
        self.ui_selector = Ui_Form()

        self.ui_selector.setupUi(self)
        self.view.parameters_window1 = [None, None, None, None, None] #form,horizontal para, vertical para, color, color para
        #self.window2_parameters = (None, None, None, None, None)
        #self.window3_parameters = (None, None, None, None, None)
        #self.window4_parameters = (None, None, None, None, None)

        #Window1
        self.ui_selector.ColorComboBox_a.currentIndexChanged.connect(self.update_color_window1)
        self.ui_selector.SizeParameterComboBox_a.currentIndexChanged.connect(self.update_sizeParameter_window1)
        #self.ui_selector.ColorComboBox_a.currentIndexChanged.connect(self.update_Window1_para)
        #self.ui_selector.ColorComboBox_a.currentIndexChanged.connect(self.updateWindow1_para)



        self.show()

    def update_color_window1(self):
        self.view.parameters_window1[3]=self.ui_selector.ColorComboBox_a.currentText()
        print(self.window1_parameters)

    def update_sizeParameter_window1(self):
        self.view.parameters_window1[2]=self.ui_selector.SizeParameterComboBox_a.currentText()
        print(self.window1_parameters)

