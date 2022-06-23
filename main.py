from PyQt5 import QtWidgets
from cls_main_from import cls_main_from
import sys
app = QtWidgets.QApplication([])
main_f = cls_main_from()
main_f.show()

sys.exit(app.exec_())