#---NOTES---#
# in qt, the side menu frames have a layout of:
# LayoutLeftmargin: 15
# LayoutTopmargin: 15
# LayoutRightmargin: 0 # Because it has to connect to the edge of frame for the #TODO: side menu active effect
# LayoutBottommargin: 15


#----#FIXME: fix imports-----#
import sys

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('untitled_2.ui', self)

    #----Are they needed?----#
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # #set app window icon
        # self.setWindowIcon(QtGui.QIcon("icon.png"))
        
        #set app window size
        # self.setGeometry(0, 0, 800, 600)
        

        # #Open window in center of screen
        # self.screenResolution = app.desktop().screenGeometry()

        #Set window to have a grid layout
        

        # self.centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()

        # # move the window to the center of the screen
        # MainWindow.move(self.centerPoint.x() - MainWindow.width() / 2, self.centerPoint.y() - MainWindow.height() / 2)

        # self.splitter1 = QSplitter(QtCore.Qt.Horizontal)
        # self.splitter1.addWidget(self.sideMenuFr)
        # self.splitter1.addWidget(self.mainContentFr)

        # self.splitter1.show()

        self.todoList = self.todoListWidget

        self.inProgressList = self.inProgressListWidget
        self.doneList = self.doneListWidget
        
        self.add_todo_button = QPushButton(self)
        self.add_todo_button.setText("Add Item")
        self.add_todo_button.clicked.connect(self.add_item_todo)

    def add_item_todo(self):
        text, ok = QInputDialog.getText(self, 'Add Item', 'Enter item:')
        if ok:
            self.todoList.addItem(text)
    
        self.todoList.itemSelectionChanged.connect(self.start_drag)

    def start_drag(self):
        item = self.todoList.currentItem()
        if item:
            mimeData = QMimeData()
            mimeData.setText(item.text())
            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.exec_(QtCore.Qt.MoveAction)

    def move_to_inProgress(self, event):
        source = event.source()
        if source == self.todoList:
            self.inProgressList.addItem(event.mimeData().text())
        elif source == self.doneList:
            self.inProgressList.addItem(event.mimeData().text())
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())