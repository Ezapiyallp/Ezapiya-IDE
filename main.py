from PyQt5 import QtWidgets, QtCore
from cls_main_from import cls_main_from
import sys
import os
app = QtWidgets.QApplication([])
print("current path is "+os.getcwd())
main_f = cls_main_from()
main_f.setWindowState(QtCore.Qt.WindowMaximized)
main_f.show()
main_f.setWindowTitle("Ezapiya-IDE")
sys.exit(app.exec_())
