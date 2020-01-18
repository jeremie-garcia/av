"""Class to display and choose parameters of figures.
Wraps a widget designed with Qt Designer"""

from PyQt5.QtWidgets import QWidget
from selector_ui import Ui_Selector


class Selector(QWidget):
    """Widget displaying selection parameters"""

    def __init__(self, the_view):
        super(Selector, self).__init__()

        self.zoom_view = the_view.zoomview
        self.view = the_view
        self.sound = the_view.sound
        self.ui_selector = Ui_Selector()
        self.ui_selector.setupUi(self)

        # list of the current parameters of the combo box
        self.comboBox_list = [[self.ui_selector.FormComboBox_1, self.ui_selector.HorizontalSizeParameterComboBox_1,
                               self.ui_selector.VerticalSizeParameterComboBox_1, self.ui_selector.ColorComboBox_1,
                               self.ui_selector.ColorParameterComboBox_1],
                              [self.ui_selector.FormComboBox_2, self.ui_selector.HorizontalSizeParameterComboBox_2,
                               self.ui_selector.VerticalSizeParameterComboBox_2, self.ui_selector.ColorComboBox_2,
                               self.ui_selector.ColorParameterComboBox_2],
                              [self.ui_selector.FormComboBox_3, self.ui_selector.HorizontalSizeParameterComboBox_3,
                               self.ui_selector.VerticalSizeParameterComboBox_3, self.ui_selector.ColorComboBox_3,
                               self.ui_selector.ColorParameterComboBox_3],
                              [self.ui_selector.FormComboBox_4, self.ui_selector.HorizontalSizeParameterComboBox_4,
                               self.ui_selector.VerticalSizeParameterComboBox_4, self.ui_selector.ColorComboBox_4,
                               self.ui_selector.ColorParameterComboBox_4]]
        self.set_combo_boxes()

        # figures status update
        for i in range(1, len(self.comboBox_list)):
            self.comboBox_list[i][0].currentIndexChanged.connect(self.update_figures_status)

        # ComboBox connection for updates of figures parameters
        for i in range(len(self.comboBox_list)):
            for j in range(len(self.comboBox_list[0])):
                self.comboBox_list[i][j].currentIndexChanged.connect(self.update_figures_parameters)

        # Sound ComboBox connection
        self.ui_selector.SoundComboBox.currentIndexChanged.connect(self.update_sound)
        self.ui_selector.SoundComboBox.currentIndexChanged.connect(self.sound_changed)

        for i in range(len(self.comboBox_list)):
            self.comboBox_list[i][0].currentIndexChanged.connect(self.form_changed)

    def set_combo_boxes(self):
        """Filling comboBoxes"""
        self.ui_selector.SoundComboBox.addItems(self.sound.sounds_dictionary)
        for i in range(len(self.comboBox_list)):
            for j in range(len(self.comboBox_list[0])):
                if j == 0:
                    self.comboBox_list[i][j].addItems(self.view.forms)
                elif j == 3:
                    self.comboBox_list[i][j].addItems(self.view.color_dict)
                else:
                    self.comboBox_list[i][j].addItems(self.view.sound_parameters)
                self.comboBox_list[i][j].setCurrentText(self.view.figures_parameters[i][j])  # presettings
        self.ui_selector.FormComboBox_1.removeItem(0)

    # setting the number of windows
    def update_figures_status(self):
        """Updates if a figure is active or not"""
        for i in range(1, len(self.comboBox_list)):
            self.view.figures_status[i] = self.comboBox_list[i][0].currentText() != 'None'
        self.view.figures_constructor()

    def update_figures_parameters(self):
        """Updates figures parameters when combobox updates"""
        for i in range(len(self.comboBox_list)):
            for j in range(len(self.comboBox_list[0])):
                self.view.figures_parameters[i][j] = self.comboBox_list[i][j].currentText()

    # sound_update
    def update_sound(self):
        """Updates sound when combobox updates"""
        self.sound.filename = self.sound.sounds_dictionary[self.ui_selector.SoundComboBox.currentText()]

    def sound_changed(self):
        """Updates sound status"""
        self.view.isSoundChanged = True
        self.view.isSoundPlayed = False

    def form_changed(self):
        """Updates form status"""
        self.view.isSoundPlayed = False
        self.view.isFormChanged = True

