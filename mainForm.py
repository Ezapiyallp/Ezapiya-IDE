# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Ezapiya-IDE_in_python\mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 773)
        MainWindow.setStyleSheet("background-color: rgb(76, 76, 76);\n"
"color: rgb(255, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: rgb(94, 94, 94);")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 33))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.menubar.setPalette(palette)
        self.menubar.setStyleSheet("QMenuBar {\n"
"background-color: rgb(64, 64, 64);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(58, 58, 58);\n"
"font: 75 16pt \"Calibri\";\n"
"}\n"
"QMenuBar::item {\n"
"color : white;\n"
"margin-top:4px;\n"
"spacing: 3px;\n"
"padding: 1px 10px;\n"
"background: transparent;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:hover {\n"
"background: blue;\n"
"color:red;\n"
"}\n"
"")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet("QMenu{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QMenu::hover{\n"
"color: #000;\n"
"}")
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.menuEdit.setObjectName("menuEdit")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setStyleSheet("color: rgb(255, 255, 255);")
        self.menuRun.setObjectName("menuRun")
        self.menuDebuge = QtWidgets.QMenu(self.menubar)
        self.menuDebuge.setStyleSheet("color: rgb(255, 255, 255);")
        self.menuDebuge.setObjectName("menuDebuge")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setStyleSheet("color: rgb(255, 255, 255);")
        self.menuSetting.setObjectName("menuSetting")
        self.menuAbout_Us = QtWidgets.QMenu(self.menubar)
        self.menuAbout_Us.setStyleSheet("color: rgb(255, 255, 255);")
        self.menuAbout_Us.setObjectName("menuAbout_Us")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setStyleSheet("color: rgb(255, 255, 255);")
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setStyleSheet("color: rgb(255, 255, 255);")
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.toolBar.setPalette(palette)
        self.toolBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolBar.setMouseTracking(True)
        self.toolBar.setStyleSheet("QToolButton:!hover {background-color:rgb(30,30, 30)} QToolBar {background:rgb(64, 64, 64)}\n"
"")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget_message = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_message.setMinimumSize(QtCore.QSize(89, 150))
        self.dockWidget_message.setStyleSheet("QDockWidget\n"
"{\n"
"background : lightgreen;\n"
"}\n"
"QDockWidget::title\n"
"{\n"
"background : lightblue;\n"
"}\n"
"QDockWidget QPushButton\n"
"{\n"
"border : 2px solid black;\n"
"background : darkgreen;\n"
"}\n"
"")
        self.dockWidget_message.setFloating(False)
        self.dockWidget_message.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.dockWidget_message.setObjectName("dockWidget_message")
        self.dockWidgetContents_message = QtWidgets.QWidget()
        self.dockWidgetContents_message.setObjectName("dockWidgetContents_message")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_message)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtmessage = QtWidgets.QTextEdit(self.dockWidgetContents_message)
        self.txtmessage.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.txtmessage.setObjectName("txtmessage")
        self.verticalLayout.addWidget(self.txtmessage)
        self.dockWidget_message.setWidget(self.dockWidgetContents_message)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_message)
        self.dockWidget_tools = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_tools.setMinimumSize(QtCore.QSize(150, 40))
        self.dockWidget_tools.setStyleSheet("QDockWidget\n"
"{\n"
"background : lightgreen;\n"
"}\n"
"QDockWidget::title\n"
"{\n"
"background : lightblue;\n"
"}\n"
"QDockWidget QPushButton\n"
"{\n"
"border : 2px solid black;\n"
"background : darkgreen;\n"
"}\n"
"")
        self.dockWidget_tools.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_tools.setObjectName("dockWidget_tools")
        self.dockWidgetContents_tools = QtWidgets.QWidget()
        self.dockWidgetContents_tools.setObjectName("dockWidgetContents_tools")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_tools)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dockWidget_tools.setWidget(self.dockWidgetContents_tools)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_tools)
        self.dockWidget_project = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_project.setMinimumSize(QtCore.QSize(150, 111))
        self.dockWidget_project.setStyleSheet("QDockWidget\n"
"{\n"
"background : lightgreen;\n"
"}\n"
"QDockWidget::title\n"
"{\n"
"background : lightblue;\n"
"}\n"
"QDockWidget QPushButton\n"
"{\n"
"border : 2px solid black;\n"
"background : darkgreen;\n"
"}\n"
"")
        self.dockWidget_project.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_project.setObjectName("dockWidget_project")
        self.dockWidgetContents_project = QtWidgets.QWidget()
        self.dockWidgetContents_project.setObjectName("dockWidgetContents_project")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_project)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeView = QtWidgets.QTreeView(self.dockWidgetContents_project)
        self.treeView.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: italic 14pt \"Arial\";")
        self.treeView.setObjectName("treeView")
        self.verticalLayout_3.addWidget(self.treeView)
        self.dockWidget_project.setWidget(self.dockWidgetContents_project)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_project)
        self.dockWidget_preproty = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_preproty.setMinimumSize(QtCore.QSize(150, 40))
        self.dockWidget_preproty.setStyleSheet("QDockWidget\n"
"{\n"
"background : lightgreen;\n"
"}\n"
"QDockWidget::title\n"
"{\n"
"background : lightblue;\n"
"}\n"
"QDockWidget QPushButton\n"
"{\n"
"border : 2px solid black;\n"
"background : darkgreen;\n"
"}\n"
"")
        self.dockWidget_preproty.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_preproty.setObjectName("dockWidget_preproty")
        self.dockWidgetContents_property = QtWidgets.QWidget()
        self.dockWidgetContents_property.setObjectName("dockWidgetContents_property")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_property)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dockWidget_preproty.setWidget(self.dockWidgetContents_property)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_preproty)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionNew.setFont(font)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/open_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folder.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionOpen_Folder.setFont(font)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_File.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionSave_File.setFont(font)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/save_as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionSave_As.setFont(font)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose_File = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/photo/1x/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose_File.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionClose_File.setFont(font)
        self.actionClose_File.setObjectName("actionClose_File")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/photo/1x/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionCut.setFont(font)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionCopy.setFont(font)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/paste1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionPaste.setFont(font)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/icon/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon9)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionUndo.setFont(font)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/icon/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon10)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionRedo.setFont(font)
        self.actionRedo.setObjectName("actionRedo")
        self.actionFind = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/icon/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon11)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionFind.setFont(font)
        self.actionFind.setObjectName("actionFind")
        self.actionReplace = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icon/icon/replace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReplace.setIcon(icon12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionReplace.setFont(font)
        self.actionReplace.setObjectName("actionReplace")
        self.actionGogo = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icon/icon/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGogo.setIcon(icon13)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionGogo.setFont(font)
        self.actionGogo.setObjectName("actionGogo")
        self.actionCompile = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icon/icon/compail_and_run.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompile.setIcon(icon14)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionCompile.setFont(font)
        self.actionCompile.setObjectName("actionCompile")
        self.actionRun = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icon/icon/walk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon15)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionRun.setFont(font)
        self.actionRun.setObjectName("actionRun")
        self.actionCompile_And_Run = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icon/photo/1x/compail_and_run.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompile_And_Run.setIcon(icon16)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionCompile_And_Run.setFont(font)
        self.actionCompile_And_Run.setObjectName("actionCompile_And_Run")
        self.actionStart_Debug = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icon/photo/1x/adb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart_Debug.setIcon(icon17)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionStart_Debug.setFont(font)
        self.actionStart_Debug.setObjectName("actionStart_Debug")
        self.actionExecute_Next_Line = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionExecute_Next_Line.setFont(font)
        self.actionExecute_Next_Line.setObjectName("actionExecute_Next_Line")
        self.actionExecute_Next_Function = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionExecute_Next_Function.setFont(font)
        self.actionExecute_Next_Function.setObjectName("actionExecute_Next_Function")
        self.actionGoto_Next_Breakpoint = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionGoto_Next_Breakpoint.setFont(font)
        self.actionGoto_Next_Breakpoint.setObjectName("actionGoto_Next_Breakpoint")
        self.actionEnd_Debug = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionEnd_Debug.setFont(font)
        self.actionEnd_Debug.setObjectName("actionEnd_Debug")
        self.actionBreakpoint = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionBreakpoint.setFont(font)
        self.actionBreakpoint.setObjectName("actionBreakpoint")
        self.actionWatch = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionWatch.setFont(font)
        self.actionWatch.setObjectName("actionWatch")
        self.actionMessage_Window = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icon/icon/icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMessage_Window.setIcon(icon18)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionMessage_Window.setFont(font)
        self.actionMessage_Window.setObjectName("actionMessage_Window")
        self.actiontool_Window = QtWidgets.QAction(MainWindow)
        self.actiontool_Window.setIcon(icon18)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actiontool_Window.setFont(font)
        self.actiontool_Window.setObjectName("actiontool_Window")
        self.actionProject_Windows = QtWidgets.QAction(MainWindow)
        self.actionProject_Windows.setIcon(icon18)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionProject_Windows.setFont(font)
        self.actionProject_Windows.setObjectName("actionProject_Windows")
        self.actionProparty_Window = QtWidgets.QAction(MainWindow)
        self.actionProparty_Window.setIcon(icon18)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionProparty_Window.setFont(font)
        self.actionProparty_Window.setObjectName("actionProparty_Window")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionSelect_All.setFont(font)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_File)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionReplace)
        self.menuEdit.addAction(self.actionGogo)
        self.menuRun.addAction(self.actionCompile)
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionRun)
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionCompile_And_Run)
        self.menuDebuge.addAction(self.actionStart_Debug)
        self.menuDebuge.addAction(self.actionExecute_Next_Line)
        self.menuDebuge.addAction(self.actionExecute_Next_Function)
        self.menuDebuge.addAction(self.actionGoto_Next_Breakpoint)
        self.menuDebuge.addAction(self.actionEnd_Debug)
        self.menuDebuge.addAction(self.actionBreakpoint)
        self.menuDebuge.addAction(self.actionWatch)
        self.menuView.addAction(self.actionMessage_Window)
        self.menuView.addAction(self.actiontool_Window)
        self.menuView.addAction(self.actionProject_Windows)
        self.menuView.addAction(self.actionProparty_Window)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuDebuge.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuAbout_Us.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave_File)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFind)
        self.toolBar.addAction(self.actionReplace)
        self.toolBar.addAction(self.actionGogo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCompile)
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuDebuge.setTitle(_translate("MainWindow", "Debug"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuAbout_Us.setTitle(_translate("MainWindow", "About Us"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dockWidget_message.setWindowTitle(_translate("MainWindow", "Message Window"))
        self.dockWidget_tools.setWindowTitle(_translate("MainWindow", "Tools Box"))
        self.dockWidget_project.setWindowTitle(_translate("MainWindow", "Project Window"))
        self.dockWidget_preproty.setWindowTitle(_translate("MainWindow", "Property Window"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setIconText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder"))
        self.actionSave_File.setText(_translate("MainWindow", "Save"))
        self.actionSave_File.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Alt+Ś"))
        self.actionClose_File.setText(_translate("MainWindow", "Close File"))
        self.actionClose_File.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionFind.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionReplace.setText(_translate("MainWindow", "Replace"))
        self.actionReplace.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionGogo.setText(_translate("MainWindow", "Goto"))
        self.actionGogo.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionCompile.setText(_translate("MainWindow", "Compile"))
        self.actionCompile.setShortcut(_translate("MainWindow", "F3"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionRun.setShortcut(_translate("MainWindow", "F4"))
        self.actionCompile_And_Run.setText(_translate("MainWindow", "Compile And Run"))
        self.actionCompile_And_Run.setShortcut(_translate("MainWindow", "F5"))
        self.actionStart_Debug.setText(_translate("MainWindow", "Start Debug"))
        self.actionStart_Debug.setShortcut(_translate("MainWindow", "F6"))
        self.actionExecute_Next_Line.setText(_translate("MainWindow", "Execute Next Line"))
        self.actionExecute_Next_Line.setShortcut(_translate("MainWindow", "F7"))
        self.actionExecute_Next_Function.setText(_translate("MainWindow", "Execute Next Function"))
        self.actionExecute_Next_Function.setShortcut(_translate("MainWindow", "F8"))
        self.actionGoto_Next_Breakpoint.setText(_translate("MainWindow", "Goto Next Breakpoint"))
        self.actionGoto_Next_Breakpoint.setShortcut(_translate("MainWindow", "F9"))
        self.actionEnd_Debug.setText(_translate("MainWindow", "End Debug"))
        self.actionEnd_Debug.setShortcut(_translate("MainWindow", "F10"))
        self.actionBreakpoint.setText(_translate("MainWindow", "Breakpoint"))
        self.actionBreakpoint.setShortcut(_translate("MainWindow", "F11"))
        self.actionWatch.setText(_translate("MainWindow", "Watch"))
        self.actionWatch.setShortcut(_translate("MainWindow", "F12"))
        self.actionMessage_Window.setText(_translate("MainWindow", "Message Window"))
        self.actiontool_Window.setText(_translate("MainWindow", "Tools Box"))
        self.actionProject_Windows.setText(_translate("MainWindow", "Project Windows"))
        self.actionProparty_Window.setText(_translate("MainWindow", "Property Window"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionSelect_All.setShortcut(_translate("MainWindow", "Ctrl+A"))

