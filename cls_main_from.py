from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize

from mainForm import Ui_MainWindow
import icon_qrc
class cls_main_from(QtWidgets.QMainWindow):
    def __init__(self):
        super(cls_main_from, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dockWidget_message.setFloating(False)
