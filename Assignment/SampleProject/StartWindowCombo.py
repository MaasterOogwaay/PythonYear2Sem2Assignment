from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from PyQT5_Ex1 import *

app = QApplication([])
w=QMainWindow()
w.setWindowTitle('Incrementer')
ex = Ui_MainWindow()
ex.setupUi(w)
w.resize(500,800)
w.show()
app.exec_()