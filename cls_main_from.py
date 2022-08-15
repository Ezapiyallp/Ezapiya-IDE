import subprocess
import os
from subprocess import Popen, PIPE
from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog,QLineEdit
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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


        self.findLineEdit = QLineEdit(self)
        self.findLineEdit.setFixedWidth(200)
        self.findLineEdit.setFixedHeight(30)
        self.findLineEdit.setFont(QFont('SansSerif', 14))
        self.findLineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.toolBar.insertWidget(self.ui.actionFind,self.findLineEdit)

        self.replaceLineEdit = QLineEdit(self)
        self.replaceLineEdit.setFixedWidth(200)
        self.replaceLineEdit.setFixedHeight(30)
        self.replaceLineEdit.setFont(QFont('SansSerif', 14))
        self.replaceLineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.toolBar.insertWidget(self.ui.actionReplace, self.replaceLineEdit)

        self.GotoLineEdit = QLineEdit(self)
        self.GotoLineEdit.setFixedWidth(100)
        self.GotoLineEdit.setFixedHeight(30)
        self.GotoLineEdit.setFont(QFont('SansSerif', 14))
        self.GotoLineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.ui.toolBar.insertWidget(self.ui.actionGogo, self.GotoLineEdit)



        self.ui.dockWidget_message.setFloating(False)
        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.removeTab(0)
        self.tabCount = 2
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

        self.ui.dockWidget_tools.setVisible(False)
        self.ui.dockWidget_project.setVisible(False)
        self.ui.dockWidget_preproty.setVisible(False)
        self.erronOnCompial=False
    def closeTab (self, currentIndex):
        self.ui.tabWidget.removeTab(currentIndex)
        self.tabCount = self.tabCount - 1
        if currentIndex==0 and self.tabCount==-1 :
            self.editor.setText("")
            self.ui.tabWidget.addTab(self.editor, 'New File')
            self.tabCount = self.tabCount + 1

    def changeTitalofActiveTab(self,tital):
        self.ui.tabWidget.setWindowTitle("dsfsdfdsfds")
        self.ui.tabWidget.setTabText(self.ui.tabWidget.currentIndex(),tital)

    def newfile_action(self):
        tfileName='New File'+str(self.tabCount)
        self.editor = SimplePythonEditor()
        self.editor.setText("")
        self.editor.setFullFileNmae(tfileName)
        self.ui.tabWidget.addTab(self.editor, tfileName)
        self.tabCount = self.tabCount + 1

    def getActiveTabIndex(self):
        yy = self.ui.tabWidget.currentWidget()
        for i in range(0,self.ui.tabWidget.count()):
            xx = self.ui.tabWidget.widget(i)
            if yy.getFullFileName() == xx.getFullFileName():
                break
        print(i)
        return i
    def openfile_action(self):
        ne = SimplePythonEditor()

        fileName = QFileDialog.getOpenFileName()
        fullFileName = fileName[0]
        status=0
        for i in range(0, self.ui.tabWidget.count()):
            xx = self.ui.tabWidget.widget(i)
            if fullFileName == xx.getFullFileName():
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
    def openfile_form_command_line_action(self,fileName):
        print(fileName)
        #self.closeTab(0)
        ne = SimplePythonEditor()
        fileTital = ne.openFile_form_command_line(fileName)
        tfileName = fileTital
        tfileName = tfileName.split('/')
        fileName = tfileName[len(tfileName) - 1]
        self.ui.tabWidget.addTab(ne, fileName)
        self.tabCount = self.tabCount + 1
        self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.count() - 1)

    def open_folder_action(self):
        pass

    def savefile_actoin(self):
        i = self.getActiveTabIndex()
        xx = self.ui.tabWidget.widget(i)
        status = xx.getSaveStatus()
        if status == "Yes":
            ff=xx.getFullFileName()
            try:
                f = open(xx.getFullFileName(), "w")
                f.write(xx.text())
                f.close()
            except Exception as e:
                print(e)
        else:
            try:
                fileName = QFileDialog.getSaveFileName()
                xx.saveFile(fileName)
                tfileName = fileName[0].split('/')
                fileName = tfileName[len(tfileName) - 1]
                self.ui.tabWidget.setTabText(self.getActiveTabIndex(), fileName)
            except Exception as e:
                print(e)

    def save_as_action(self):
        i = self.getActiveTabIndex()
        xx = self.ui.tabWidget.widget(i)
        fileName = QFileDialog.getSaveFileName()
        xx.saveFile(fileName)
        tfileName = fileName[0].split('/')
        fileName = tfileName[len(tfileName) - 1]
        self.ui.tabWidget.setTabText(self.getActiveTabIndex(), fileName)

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
        i = self.getActiveTabIndex()
        xx = self.ui.tabWidget.widget(i)
        xx.selectAll()
    def undo_action(self):
        i = self.getActiveTabIndex()
        xx = self.ui.tabWidget.widget(i)
        xx.undo()
    def redo_action(self):
        i = self.getActiveTabIndex()
        xx = self.ui.tabWidget.widget(i)
        xx.redo()

    def find_actio(self):

        i = self.getActiveTabIndex()
        xx = self.ui.tabWidget.widget(i)
        textToFind= self.findLineEdit.text()
        if textToFind=="":
            self.findLineEdit.setFocus()
        else:
            SaveStatus = xx.findFunction(textToFind,True)



    def replace_action(self):
        print("replace")

    def goto_action(self):
        print("goto")


        ##### View Mune All Action
    def message_window_action(self):
            if self.message_window_status==True:
                self.ui.dockWidget_message.setVisible(False)
                self.message_window_status = False
                self.ui.actionMessage_Window.setIconVisibleInMenu(False)
            else:
                self.ui.dockWidget_message.setVisible(True)
                self.message_window_status = True
                self.ui.actionMessage_Window.setIconVisibleInMenu(True)

    def tool_box_action(self):
        pass
        # if self.tool_box_status == True:
        #     self.ui.dockWidget_tools.setVisible(False)
        #     self.tool_box_status = False
        #     self.ui.actiontool_Window.setIconVisibleInMenu(False)
        # else:
        #     self.ui.dockWidget_tools.setVisible(True)
        #     self.tool_box_status = True
        #     self.ui.actiontool_Window.setIconVisibleInMenu(True)

    def project_window_action(self):
        pass
        # if self.project_window_status == True:
        #     self.ui.dockWidget_project.setVisible(False)
        #     self.project_window_status =False
        #     self.ui.actionProject_Windows.setIconVisibleInMenu(False)
        # else:
        #     self.ui.dockWidget_project.setVisible(True)
        #     self.project_window_status = True
        #     self.ui.actionProject_Windows.setIconVisibleInMenu(True)

    def property_window_action(self):
        pass
        # if self.project_window_status == True:
        #     self.ui.dockWidget_preproty.setVisible(False)
        #     self.property_window_status = False
        #     self.ui.actionProparty_Window.setIconVisibleInMenu(False)
        # else:
        #     self.ui.dockWidget_preproty.setVisible(True)
        #     self.property_window_status = True
        #     self.ui.actionProparty_Window.setIconVisibleInMenu(True)

        ##### Run Mune All Action
    def compile_action(self):

        self.erronOnCompial=True
        i = self.getActiveTabIndex()
        xx = self.ui.tabWidget.widget(i)
        SaveStatus=xx.getSaveStatus()
        if SaveStatus=="Yes":
            xfn=xx.getFullFileName()
            print("xfn is" +xfn)
            extentions = xfn.split('.')
            extention = extentions[len(extentions) - 1]
            if extention=='c':
                yfn=xfn.replace(".c",".exe")
                print("yfn is" + yfn)
                os.environ["gcc"] = r"C:\Users\vinit\AppData\Roaming\Ezapiya\MinGW\bin\gcc.exe"
                p = Popen(['gcc', '-g', xfn, '-o', yfn, '-static'], stdin=PIPE,
                      stdout=PIPE, stderr=PIPE)
                output, err = p.communicate()
                rc = p.returncode
                output=output.decode("utf-8")
                err = err.decode("utf-8")
                print("output " + str(output))
                print("err " + str(err))
                self.ui.txtmessage.setText(str(output)+str(err))
                if str(err)=="":
                    self.erronOnCompial=False
                else:
                    self.erronOnCompial=True
            if extention == 'cpp' or extention == 'c++' :
                yfn = xfn.replace(".cpp", ".exe")
                print("yfn is" + yfn)
                os.environ["g++"] = r"C:\Users\vinit\AppData\Roaming\Ezapiya\MinGW\bin\g++.exe"
                p = Popen(['g++', '-g', xfn, '-o', yfn, '-static'], stdin=PIPE,
                          stdout=PIPE, stderr=PIPE)
                output, err = p.communicate()
                rc = p.returncode
                output = output.decode("utf-8")
                err = err.decode("utf-8")
                print("output " + str(output))
                print("err " + str(err))
                self.ui.txtmessage.setText(str(output) + str(err))
                if str(err) == "":
                    self.erronOnCompial = False
                else:
                    self.erronOnCompial = True
        if SaveStatus=="No":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File is Not Save. Do you want to save this file")
            msg.setWindowTitle("Ezapiya IDE")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            #msg.buttonClicked.connect(self.msgbtn)
            retval = msg.exec_()
            if retval == QMessageBox.Yes :
                self.savefile_actoin()



    def run_action(self):
        self.compile_action()
        if self.erronOnCompial==False:
            i = self.getActiveTabIndex()
            xx = self.ui.tabWidget.widget(i)
            xfn = xx.getFullFileName()
            print("xfn="+str(xfn))
            file_path=os.path.dirname(os.path.abspath(xfn))
            xfn=xfn.replace('\\','/')
            fileNames = xfn.split('/')
            fileName = fileNames[len(fileNames) - 1]

            extentions = fileName.split('.')
            finalFileName = extentions[len(extentions) - 2]

            output_exe=file_path+"\\"+finalFileName+".exe"
            print("output_exe=" + str(output_exe))
            appDataPath = os.getenv('APPDATA')
            CCpath = os.path.join(appDataPath, "Ezapiya")

            data_for_batch_file = "@ECHO OFF \n"
            data_for_batch_file = data_for_batch_file + "cd " + file_path + "\n"
            data_for_batch_file = data_for_batch_file + "\"" + output_exe + "\"\n"
            data_for_batch_file = data_for_batch_file + "cd " + CCpath+"\n"
            data_for_batch_file = data_for_batch_file + "\nstop_.exe"
            batFileName=CCpath+"\\run.bat"
            f = open(batFileName, "w")
            f.write(data_for_batch_file)
            f.close()
            p = subprocess.Popen(batFileName, creationflags=subprocess.CREATE_NEW_CONSOLE)


    def compile_and_run_action(self):
        self.erronOnCompial = True
        i = self.getActiveTabIndex()
        xx = self.ui.tabWidget.widget(i)
        SaveStatus = xx.getSaveStatus()
        if SaveStatus == "Yes":
            xfn = xx.getFullFileName()
            print("xfn is" + xfn)
            extentions = xfn.split('.')
            extention = extentions[len(extentions) - 1]
            if extention == 'py':
                #os.environ["python"] = r"C:\Users\vinit\AppData\Local\Programs\Python\Python38\python.exe"
                #p = Popen(['python',  xfn, ], )
                appDataPath = os.getenv('APPDATA')
                CCpath = os.path.join(appDataPath, "Ezapiya")
                data_for_batch_file = "@ECHO OFF \n"
                data_for_batch_file = data_for_batch_file + "python " + xfn + "\n"
                data_for_batch_file = data_for_batch_file + "\nstop_.exe"
                batFileName = CCpath + "\\run.bat"
                f = open(batFileName, "w")
                f.write(data_for_batch_file)
                f.close()
                p = subprocess.Popen(batFileName, creationflags=subprocess.CREATE_NEW_CONSOLE)

        if SaveStatus == "No":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File is Not Save. Do you want to save this file")
            msg.setWindowTitle("Ezapiya IDE")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            # msg.buttonClicked.connect(self.msgbtn)
            retval = msg.exec_()
            if retval == QMessageBox.Yes:
                self.savefile_actoin()

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

