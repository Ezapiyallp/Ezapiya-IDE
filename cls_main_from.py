from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QFileDialog
import sys
from mainForm import Ui_MainWindow
from SimplePythonEditor import SimplePythonEditor
import icon_qrc
class cls_main_from(QtWidgets.QMainWindow):
    def __init__(self):
        super(cls_main_from, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.message_window_status = True
        self.tool_box_status = True
        self.project_window_status = True
        self.property_window_status = True

        self.ui.dockWidget_message.setFloating(False)
        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.removeTab(0)
        self.tabCount = 2

        #self.ui.tabWidget.tabCloseRequested.connect(self.closeActiveTab)
        self.ui.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.editor = SimplePythonEditor()
        self.ui.tabWidget.addTab(self.editor, 'New File 1')
            #### File Menu all action
        self.ui.actionNew.triggered.connect(self.newfile_action)
        self.ui.actionOpen.triggered.connect(self.openfile_action)
        self.ui.actionOpen_Folder.triggered.connect(self.open_folder_action)
        self.ui.actionSave_File.triggered.connect(self.savefile_actoin)
        self.ui.actionSave_As.triggered.connect(self.save_as_action)
        self.ui.actionClose_File.triggered.connect(self.closeTab)
        self.ui.actionExit.triggered.connect(self.exit_action)

            ##### Edit mune All Action #####
        self.ui.actionCut.triggered.connect(self.cut_action)
        self.ui.actionCopy.triggered.connect(self.copy_action)
        self.ui.actionPaste.triggered.connect(self.paste_action)
        self.ui.actionSelect_All.triggered.connect(self.select_all_action)
        self.ui.actionUndo.triggered.connect(self.undo_action)
        self.ui.actionRedo.triggered.connect(self.redo_action)
        self.ui.actionFind.triggered.connect(self.find_actio)
        self.ui.actionReplace.triggered.connect(self.replace_action)
        self.ui.actionGogo.triggered.connect(self.goto_action)
                ##### View Mune All Action
        self.ui.actionMessage_Window.triggered.connect(self.message_window_action)
        self.ui.actiontool_Window.triggered.connect(self.tool_box_action)
        self.ui.actionProject_Windows.triggered.connect(self.project_window_action)
        self.ui.actionProparty_Window.triggered.connect(self.property_window_action)
                    ##### Run Mune All Action
        self.ui.actionCompile.triggered.connect(self.compile_action)
        self.ui.actionRun.triggered.connect(self.run_action)
        self.ui.actionCompile_And_Run.triggered.connect(self.compile_and_run_action)
                    ###### Debug Mune All Action
        self.ui.actionStart_Debug.triggered.connect(self.start_debug_action)
        self.ui.actionExecute_Next_Line.triggered.connect(self.execute_next_line_action)
        self.ui.actionExecute_Next_Function.triggered.connect(self.execute_next_funtion_action)
        self.ui.actionGoto_Next_Breakpoint.triggered.connect(self.goto_next_breackpoint_action)
        self.ui.actionEnd_Debug.triggered.connect(self.end_debug_action)
        self.ui.actionBreakpoint.triggered.connect(self.breackpoint_action)
        self.ui.actionWatch.triggered.connect(self.watch_action)

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
        tfileName='New File'+str(self.tabCount)
        self.editor = SimplePythonEditor()
        self.editor.setText("")
        self.editor.setFullFileNmae(tfileName)
        self.ui.tabWidget.addTab(self.editor, tfileName)
        self.tabCount = self.tabCount + 1
        #self.ui.tabWidget.currentWidget()
    def getActiveTabIndex(self):
        yy=self.ui.tabWidget.currentWidget()
        for i in range(0,self.ui.tabWidget.count()):
            xx = self.ui.tabWidget.widget(i)
            if yy.getFullFileName()==xx.getFullFileName():
                break
        print(i)
        return i
    def openfile_action(self):
        ne= SimplePythonEditor()
        #self.ne.setTabID(self.TabId)
        #self.ne.TabID=self.TabId
        fileName = QFileDialog.getOpenFileName()
        fullFileName = fileName[0]
        status=0
        for i in range(0,self.ui.tabWidget.count()):
            xx = self.ui.tabWidget.widget(i)
            if fullFileName==xx.getFullFileName():
                status = 1
                break

        if status == 1:
            self.ui.tabWidget.setCurrentIndex(i)
        else:
            fileTital= ne.openFile(fileName)
            tfileName = fileTital
            tfileName = tfileName.split('/')
            fileName = tfileName[len(tfileName) - 1]
            self.ui.tabWidget.addTab(ne, fileName)
            self.tabCount = self.tabCount + 1
            self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.count()-1)

    def open_folder_action(self):
        pass
    def savefile_actoin(self):
        fileTital=self.editor.saveFile()
        tfileName = fileTital
        tfileName = tfileName.split('/')
        fileName = tfileName[len(tfileName) - 1]
        self.changeTitalofActiveTab(fileName)
    def save_as_action(self):
        pass
    def exit_action(self):
        sys.exit()


        ###Edit Mune All Action
    def cut_action(self):
        i = self.getActiveTabIndex()
        xx = self.ui.tabWidget.widget(i)
        xx.cut()
    def copy_action(self):
        i = self.getActiveTabIndex()
        xx = self.ui.tabWidget.widget(i)
        xx.copy()

    def paste_action(self):
        i = self.getActiveTabIndex()
        xx = self.ui.tabWidget.widget(i)
        xx.paste()
    def select_all_action(self):
       print("select_all")

    def undo_action(self):
        print("undo")
    def redo_action(self):
        print("redo")
    def find_actio(self):
        print("find")
    def replace_action(self):
        print("replace")
    def goto_action(self):
        print("goto")

        ##### View Mune All Action
    def message_window_action(self):
            if self.message_window_status==True:
                self.ui.dockWidget_message.setVisible(False)
                self.message_window_status = False
            else:
                self.ui.dockWidget_message.setVisible(True)
                self.message_window_status = True
    def tool_box_action(self):
        if self.tool_box_status == True:
            self.ui.dockWidget_tools.setVisible(False)
            self.tool_box_status = False
        else:
            self.ui.dockWidget_tools.setVisible(True)
            self.tool_box_status = True
    def project_window_action(self):
        if self.project_window_status == True:
            self.ui.dockWidget_project.setVisible(False)
            self.project_window_status =False
        else:
            self.ui.dockWidget_project.setVisible(True)
            self.project_window_status = True
    def property_window_action(self):
        if self.project_window_status == True:
            self.ui.dockWidget_preproty.setVisible(False)
            self.property_window_status =False
        else:
            self.ui.dockWidget_preproty.setVisible(True)
            self.property_window_status = True

        ##### Run Mune All Action
    def compile_action(self):
        pass
        #print("compile")
    def run_action(self):
        pass
        #print("run")
    def compile_and_run_action(self):
        pass
        #print("Run and Compile")



        ###### Debug Mune All Action


    def start_debug_action(self):
        print("start")
    def execute_next_line_action(self):
        print("line")
    def execute_next_funtion_action(self):
        print("funtion")
    def goto_next_breackpoint_action(self):
        print("goto")
    def end_debug_action(self):
        print("end")
    def breackpoint_action(self):
        print("breack")
    def watch_action(self):
        print("watch")