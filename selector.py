from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListView
from selector_ui import Ui_Selector



class Selector(QWidget):
    """ Widget displaying selection parameters"""

    def __init__(self, the_view):
        super(Selector, self).__init__()

        self.view = the_view.view
        self.sound=the_view.sound
        self.ui_selector = Ui_Selector()

        self.ui_selector.setupUi(self)
        self.ui_selector.SoundComboBox.addItems(self.sound.sounds_dictionnary)

        """Window_number"""

        self.ui_selector.FormComboBox_2.currentIndexChanged.connect(self.update_window_number)
        self.ui_selector.FormComboBox_3.currentIndexChanged.connect(self.update_window_number)
        self.ui_selector.FormComboBox_4.currentIndexChanged.connect(self.update_window_number)

        """Window 1 connection ComboBox to Parameters"""
        self.ui_selector.FormComboBox_1.currentIndexChanged.connect(self.update_form_window1)
        self.ui_selector.ColorComboBox_1.currentIndexChanged.connect(self.update_color_window1)
        self.ui_selector.ColorParameterComboBox_1.currentIndexChanged.connect(self.update_colorPara_window1)
        self.ui_selector.HorizontalSizeParameterComboBox_1.currentIndexChanged.connect(self.update_horizSizePara_window1)
        self.ui_selector.VerticalSizeParameterComboBox_1.currentIndexChanged.connect(self.update_vertiSizePara_window1)

        """Window 2 connection ComboBox to Parameters"""
        self.ui_selector.FormComboBox_2.currentIndexChanged.connect(self.update_form_window2)
        self.ui_selector.ColorComboBox_2.currentIndexChanged.connect(self.update_color_window2)
        self.ui_selector.ColorParameterComboBox_2.currentIndexChanged.connect(self.update_colorPara_window2)
        self.ui_selector.HorizontalSizeParameterComboBox_2.currentIndexChanged.connect(self.update_horizSizePara_window2)
        self.ui_selector.VerticalSizeParameterComboBox_2.currentIndexChanged.connect(self.update_vertiSizePara_window2)

        """Window 3 connection ComboBox to Parameters"""
        self.ui_selector.FormComboBox_3.currentIndexChanged.connect(self.update_form_window3)
        self.ui_selector.ColorComboBox_3.currentIndexChanged.connect(self.update_color_window3)
        self.ui_selector.ColorParameterComboBox_3.currentIndexChanged.connect(self.update_colorPara_window3)
        self.ui_selector.HorizontalSizeParameterComboBox_3.currentIndexChanged.connect(self.update_horizSizePara_window3)
        self.ui_selector.VerticalSizeParameterComboBox_3.currentIndexChanged.connect(self.update_vertiSizePara_window3)

        """Window 4 connection ComboBox to Parameters"""
        self.ui_selector.FormComboBox_4.currentIndexChanged.connect(self.update_form_window4)
        self.ui_selector.ColorComboBox_4.currentIndexChanged.connect(self.update_color_window4)
        self.ui_selector.ColorParameterComboBox_4.currentIndexChanged.connect(self.update_colorPara_window4)
        self.ui_selector.HorizontalSizeParameterComboBox_4.currentIndexChanged.connect(self.update_horizSizePara_window4)
        self.ui_selector.VerticalSizeParameterComboBox_4.currentIndexChanged.connect(self.update_vertiSizePara_window4)

        """sound connection"""
        self.ui_selector.SoundComboBox.currentIndexChanged.connect(self.update_sound)

        self.show()

    """sound combo box list of sounds"""

    # Window 1 updates
    def update_form_window1(self):
        self.view.parameters_window1["form"] = self.ui_selector.FormComboBox_1.currentText()

    def update_color_window1(self):
        self.view.parameters_window1["color"] = self.ui_selector.ColorComboBox_1.currentText()

    def update_colorPara_window1(self):
        self.view.parameters_window1["colorPara"] = self.ui_selector.ColorParameterComboBox_1.currentText()

    def update_horizSizePara_window1(self):
        self.view.parameters_window1["horizPara"] = self.ui_selector.HorizontalSizeParameterComboBox_1.currentText()

    def update_vertiSizePara_window1(self):
        self.view.parameters_window1["verticPara"] = self.ui_selector.VerticalSizeParameterComboBox_1.currentText()

    """Window 2 updates"""

    def update_form_window2(self):
        self.view.parameters_window2["form"] = self.ui_selector.FormComboBox_2.currentText()

    def update_color_window2(self):
        self.view.parameters_window2["color"] = self.ui_selector.ColorComboBox_2.currentText()

    def update_colorPara_window2(self):
        self.view.parameters_window2["colorPara"] = self.ui_selector.ColorParameterComboBox_2.currentText()

    def update_horizSizePara_window2(self):
        self.view.parameters_window2["horizPara"] = self.ui_selector.HorizontalSizeParameterComboBox_2.currentText()

    def update_vertiSizePara_window2(self):
        self.view.parameters_window2["verticPara"] = self.ui_selector.VerticalSizeParameterComboBox_2.currentText()

    """Window 3 updates"""

    def update_form_window3(self):
        self.view.parameters_window3["form"] = self.ui_selector.FormComboBox_3.currentText()

    def update_color_window3(self):
        self.view.parameters_window3["color"] = self.ui_selector.ColorComboBox_3.currentText()

    def update_colorPara_window3(self):
        self.view.parameters_window3["colorPara"] = self.ui_selector.ColorParameterComboBox_3.currentText()

    def update_horizSizePara_window3(self):
        self.view.parameters_window3["horizPara"] = self.ui_selector.HorizontalSizeParameterComboBox_3.currentText()

    def update_vertiSizePara_window3(self):
        self.view.parameters_window3["verticPara"] = self.ui_selector.VerticalSizeParameterComboBox_3.currentText()

    """Window 4 updates"""

    def update_form_window4(self):
        self.view.parameters_window4["form"] = self.ui_selector.FormComboBox_4.currentText()

    def update_color_window4(self):
        self.view.parameters_window4["color"] = self.ui_selector.ColorComboBox_4.currentText()

    def update_colorPara_window4(self):
        self.view.parameters_window4["colorPara"] = self.ui_selector.ColorParameterComboBox_4.currentText()

    def update_horizSizePara_window4(self):
        self.view.parameters_window4["horizPara"] = self.ui_selector.HorizontalSizeParameterComboBox_4.currentText()

    def update_vertiSizePara_window4(self):
        self.view.parameters_window4["verticPara"] = self.ui_selector.VerticalSizeParameterComboBox_4.currentText()

    """window number update"""

    def update_window_number(self):
        if self.view.parameters_window2["form"] is not None:
            self.view.window_number_activated.append(2)
        if self.view.parameters_window3["form"] is not None:
            self.view.window_number_activated.append(3)
        if self.view.parameters_window4["form"] is not None:
            self.view.window_number_activated.append(4)

    """sound_update"""

    def update_sound(self):
        self.sound.filename = self.sound.dictionnaire_sounds[self.ui_selector.SoundComboBox.currentText()]