from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QLabel
from PyQt5 import QtWidgets
from PyQt5.QtWinExtras import QtWin
import binascii
myappid = 'kodirovka'
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
from calc import Ui_MainWindow  # импорт ui
import sys

summators_str = []
global b
b = 0
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)