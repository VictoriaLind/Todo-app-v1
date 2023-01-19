
#----#FIXME: fix imports-----#
import sys

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class main_window(QtGui.QWidget):
    def __init__(self):      
        super(main_window, self).__init__()
        
        self.setGeometry(0, 0, 800, 600)

        self.setStyleSheet("""
            QMainWindow{
                background-color: white;
            }
        """)

        # #Open window in center of screen
        # self.screenResolution = app.desktop().screenGeometry()

        #Set window to have a grid layout


        # self.centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()

        # # move the window to the center of the screen
        # MainWindow.move(self.centerPoint.x() - MainWindow.width() / 2, self.centerPoint.y() - MainWindow.height() / 2)

        self.sideMenuFr = QFrame()
        self.sideMenuFr.setStyleSheet("""
            QFrame{
                background-color: #2C3E50;
                border: none;
            }
        """)

        self.mainContentFr = QFrame()

        self.splitter1 = QSplitter(QtCore.Qt.Horizontal)
        self.splitter1.addWidget(self.sideMenuFr)
        self.splitter1.addWidget(self.mainContentFr)

        self.splitter1.show()

app=QtGui.QApplication(sys.argv)
ex=main_window()
sys.exit(app.exec_())    