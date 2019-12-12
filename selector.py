from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListView

from selector_ui import Ui_Selector

class Selector(QWidget):
    """ Widget displaying selection parameters"""

    def __init__(self, the_view):
        super(Selector, self).__init__()

        self.view = the_view
        self.ui_selector = Ui_Selector()

        self.ui_selector.setupUi(self)


        """Window 1 connection ComboBox to Parameters"""
        self.ui_selector.FormComboBox_1.currentIndexChanged.connect(self.update_form_window1)
        self.ui_selector.ColorComboBox_1.currentIndexChanged.connect(self.update_color_window1)
        self.ui_selector.ColorParameterComboBox_1.currentIndexChanged.connect(self.update_colorPara_window1)
        self.ui_selector.HorizontalSizeParameterComboBox_1.currentIndexChanged.connect(self.update_horizSizePara_window1)
        self.ui_selector.VerticalSizeParameterComboBox_1.currentIndexChanged.connect(self.update_vertiSizePara_window1)





        self.show()

    """Window 1 updates"""

    def update_form_window1(self):
        self.view.parameters_window1["form"]=self.ui_selector.FormComboBox_1.currentText()

    def update_color_window1(self):
        self.view.parameters_window1["color"]=self.ui_selector.ColorComboBox_1.currentText()

    def update_colorPara_window1(self):
        self.view.parameters_window1["colorPara"]=self.ui_selector.ColorParameterComboBox_1.currentText()

    def update_horizSizePara_window1(self):
        self.view.parameters_window1["horizPara"]=self.ui_selector.HorizontalSizeParameterComboBox_1.currentText()

    def update_vertiSizePara_window1(self):
        self.view.parameters_window1["verticPara"]=self.ui_selector.VerticalSizeParameterComboBox_1.currentText()



