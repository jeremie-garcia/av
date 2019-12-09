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

        self.show()
