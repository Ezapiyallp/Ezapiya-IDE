from PyQt5 import QtWidgets, QtCore, QtGui

from cls_main_from import cls_main_from
from cls_logoform import cls_logoform
import sys
import os
app = QtWidgets.QApplication([])
app.setWindowIcon(QtGui.QIcon('logo32into32.png'))
cwd=os.getcwd()
appDataPath=os.getenv('APPDATA')
CCpath = os.path.join(appDataPath, "Ezapiya")

if os.path.exists(CCpath):
    print("GCC is Avilable show main form")
    main_f = cls_main_from()
    main_f.setWindowState(QtCore.Qt.WindowMaximized)
    main_f.setWindowIcon(QtGui.QIcon('logo32into32.png'))
    main_f.show()
    main_f.setWindowTitle("Ezapiya-IDE")
else:
    print("GCC is Not Avilable show Logo Form")
    logo_f=cls_logoform()
    logo_f.setWindowFlags(QtCore.Qt.CustomizeWindowHint )
    logo_f.show()
    logo_f.setWindowTitle("Ezapiya-IDE")



#print("current path is "+os.getcwd())
#print(os.getenv('APPDATA'))

sys.exit(app.exec_())
