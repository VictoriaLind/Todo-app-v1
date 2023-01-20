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
        loadUi('untitled_3.ui', self)

        self.todoList = self.todoListWidget
        #add task to todolist
        self.todoList.addItem("test")
        self.todoList.addItem("test2")

        self.todoAddtaskLE = self.todoAddTaskLineEdit
        self.todoAddtaskPB = self.todoAddTaskPushButton
        
        self.inProgressList = self.inProgressListWidget
        self.inPAddtaskLE = self.inPAddTaskLineEdit
        self.inPAddtaskPB = self.inPAddTaskPushButton

        self.doneList = self.doneListWidget
        self.doneAddtaskLE = self.doneAddTaskLineEdit
        self.doneAddtaskPB = self.doneAddTaskPushButton

        self.todoAddtaskPB.clicked.connect(self.add_task_todo)
        self.inPAddtaskPB.clicked.connect(self.add_task_in_progress)
        self.doneAddtaskPB.clicked.connect(self.add_task_done)

    def add_task_todo(self):
        try:
            task_text = self.todoAddtaskLE.text()
            self.todoList.addItem(task_text)
            self.todoAddtaskLE.clear()
        except Exception as e:
            print(e)

    def add_task_in_progress(self):
        try:
            task_text = self.inPAddtaskLE.text()
            self.inProgressList.addItem(task_text)
            self.inPAddtaskLE.clear()
        except Exception as e:
            print(e)
    
    def add_task_done(self):
        try:
            task_text = self.doneAddtaskLE.text()
            self.doneList.addItem(task_text)
            self.doneAddtaskLE.clear()
        except Exception as e:
            print(e)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())