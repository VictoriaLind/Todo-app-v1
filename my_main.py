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
        loadUi('untitled.ui', self)

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
        #add task to todolist
        self.todoList.addItem("test")
        
        self.inProgressList = self.inProgressListWidget
        self.doneList = self.doneListWidget
        
        self.add_todo_button = QPushButton(self)
        self.add_todo_button.setText("Add Item")
        self.add_todo_button.clicked.connect(self.add_item_todo)


        self.inProgressList.itemSelectionChanged.connect(self.start_drag_inProgress)
        self.doneList.itemSelectionChanged.connect(self.start_drag_done)

        self.todoList.itemSelectionChanged.connect(self.start_drag_todo)
        self.todoList.dropEvent = self.move_to_inProgress
    def add_item_todo(self):
        text, ok = QInputDialog.getText(self, 'Add Item', 'Enter item:')
        if ok:
            self.todoList.addItem(text)
        
        self.inProgressList.itemPressed.connect(self.move_to_inProgress)
        self.doneList.itemPressed.connect(self.move_to_done)

    def start_drag_todo(self):
        item = self.todoList.currentItem()
        if item:
            mime_data = QMimeData()
            mime_data.setText(item.text())
            drag = QDrag(self)
            drag.setMimeData(mime_data)
            drag.exec_()
    
    def start_drag_inProgress(self):
        item = self.inProgressList.currentItem()
        if item:
            mime_data = QMimeData()
            mime_data.setText(item.text())
            drag = QDrag(self)
            drag.setMimeData(mime_data)
            drag.exec_()
    
    def start_drag_done(self):
        item = self.doneList.currentItem()
        if item:
            mime_data = QMimeData()
            mime_data.setText(item.text())
            drag = QDrag(self)
            drag.setMimeData(mime_data)
            drag.exec_()

    def move_to_inProgress(self, event):
        source = event.source()
        text = event.mimeData().text()
        if source == self.todoList:
            item = self.todoList.currentItem()
            if self.inProgressList.findItems(text, Qt.MatchExactly):
                pass
            else:
                self.inProgressList.addItem(text)
                self.todoList.takeItem(self.todoList.row(item))
        elif source == self.doneList:
            item = self.doneList.currentItem()
            if self.inProgressList.findItems(text, Qt.MatchExactly):
                pass
            else:
                self.inProgressList.addItem(text)
                self.doneList.takeItem(self.doneList.row(item))
        event.accept()

    def move_to_done(self, event):
        source = event.source()
        text = event.mimeData().text()
        if source == self.todoList:
            item = self.todoList.currentItem()
            if self.doneList.findItems(text, Qt.MatchExactly):
                pass
            else:
                self.doneList.addItem(text)
                self.todoList.takeItem(self.todoList.row(item))
        elif source == self.inProgressList:
            item = self.inProgressList.currentItem()
            if self.doneList.findItems(text, Qt.MatchExactly):
                pass
            else:
                self.doneList.addItem(text)
                self.inProgressList.takeItem(self.inProgressList.row(item))
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())