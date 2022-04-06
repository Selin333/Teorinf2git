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
    def btnClicked(self):

        get_kol_sum(self.ui.lineEdit_2.text())

        print(get_summators(self.ui.lineEdit_4.text()))
        if b ==kol_sum:
            self.ui.lineEdit_3.setText(encoding(self.ui.lineEdit.text()))


    def btnClicked_2(self):
        self.ui.lineEdit_5.setText(decoding())


        # Ошибки
        def Error(info):
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Ошибка")
            error.setInformativeText(info)
            error.setWindowTitle("Ой-йой")
            error.exec_()