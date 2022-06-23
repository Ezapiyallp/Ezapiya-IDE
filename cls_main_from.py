from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize

from mainForm import Ui_MainWindow
from SimplePythonEditor import SimplePythonEditor
import icon_qrc
class cls_main_from(QtWidgets.QMainWindow):
    def __init__(self):
        super(cls_main_from, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dockWidget_message.setFloating(False)
        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.tabCloseRequested.connect(self.closeActiveTab)
        self.editor = SimplePythonEditor()
        self.ui.tabWidget.addTab(self.editor, 'New File')
        self.ui.actionNew.triggered.connect(self.newfile_action)
    def closeActiveTab(self):
        self.ui.tabWidget.removeTab(self.ui.tabWidget.currentIndex())
        if self.ui.tabWidget.count() == 0:
            self.ui.tabWidget.addTab(self.editor, 'New File')

    def newfile_action(self):
        self.ui.tabWidget.addTab(self.editor, 'New File')