from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize

from mainForm import Ui_MainWindow
from SimplePythonEditor import SimplePythonEditor
import icon_qrc
class cls_main_from(QtWidgets.QMainWindow):
    def __init__(self):
        super(cls_main_from, self).__init__()
        self.TabId=0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dockWidget_message.setFloating(False)
        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.removeTab(0)
        #self.ui.tabWidget.tabCloseRequested.connect(self.closeActiveTab)
        self.ui.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.editor = SimplePythonEditor()

        self.ui.tabWidget.addTab(self.editor, 'New File')
        self.ui.actionNew.triggered.connect(self.newfile_action)
        self.ui.actionClose_File.triggered.connect(self.closeTab)
        self.ui.actionOpen.triggered.connect(self.openfile_action)
        self.ui.actionSave_File.triggered.connect(self.savefile_actoin)
        self.tabCount = 0

    def closeTab (self, currentIndex):
        #currentqwidget = self.ui.tabWidget(currentIndex)
        #currentqwidget.deleteLater()
        self.ui.tabWidget.removeTab(currentIndex)
        self.tabCount = self.tabCount - 1
        if currentIndex==0 and self.tabCount==-1 :
            self.editor.setText("")
            self.ui.tabWidget.addTab(self.editor, 'New File')
            self.tabCount = self.tabCount + 1

    def changeTitalofActiveTab(self,tital):
        #self.ui.tabWidget.removeTab(self.ui.tabWidget.currentIndex())
        self.ui.tabWidget.setWindowTitle("dsfsdfdsfds")
        self.ui.tabWidget.setTabText(self.ui.tabWidget.currentIndex(),tital)



    def newfile_action(self):
        self.editor = SimplePythonEditor()
        self.TabId = self.TabId + 1
        self.editor.setTabID(self.TabId)
        self.editor.setText("")
        self.ui.tabWidget.addTab(self.editor, 'New File')
        self.tabCount = self.tabCount + 1


    def openfile_action(self):
        ne= SimplePythonEditor()
        self.TabId = self.TabId + 1
        #self.ne.setTabID(self.TabId)
        #self.ne.TabID=self.TabId
        fileTital= ne.openFile()
        tfileName = fileTital
        tfileName = tfileName.split('/')
        fileName = tfileName[len(tfileName) - 1]
        self.ui.tabWidget.addTab(ne, fileName)
        self.tabCount = self.tabCount + 1
        print(self.ui.tabWidget.count())

        #xx.setText("")
        for i in range(1,self.ui.tabWidget.count()):
            xx = self.ui.tabWidget.widget(i)
            print(xx.getFullFileName())



    def savefile_actoin(self):
        fileTital=self.editor.saveFile()
        tfileName = fileTital
        tfileName = tfileName.split('/')
        fileName = tfileName[len(tfileName) - 1]
        self.changeTitalofActiveTab(fileName)
