
# ----#FIXME: fix imports-----#
import sys

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

import json


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('untitled_3.ui', self)

        self.todoList = self.todoListWidget
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

        self.load_tasks()

    def closeEvent(self, event):
        self.save_tasks()
        event.accept()

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

    def save_tasks(self):
        try:
            tasks = {}
            for i in range(self.todoList.count()):
                item = self.todoList.item(i)
                tasks[item.text()] = "todo"

            for i in range(self.inProgressList.count()):
                item = self.inProgressList.item(i)
                tasks[item.text()] = "in progress"

            for i in range(self.doneList.count()):
                item = self.doneList.item(i)
                tasks[item.text()] = "done"

            with open("tasks.json", "w") as f:
                json.dump(tasks, f)
        except FileNotFoundError:
            print("tasks.json not found. Creating a new one.")
            with open("tasks.json", "w") as f:
                json.dump({}, f)
        except json.decoder.JSONDecodeError:
            print("tasks.json is corrupted. Creating a new one.")
            with open("tasks.json", "w") as f:
                json.dump({}, f)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                tasks = json.load(f)
            for task, status in tasks.items():
                if status == "todo":
                    self.todoList.addItem(task)
                elif status == "in progress":
                    self.inProgressList.addItem(task)
                elif status == "done":
                    self.doneList.addItem(task)
        except FileNotFoundError:
            print("tasks.json not found. Creating a new one.")
            with open("tasks.json", "w") as f:
                json.dump({}, f)
        except json.decoder.JSONDecodeError:
            print("tasks.json is corrupted. Creating a new one.")
            with open("tasks.json", "w") as f:
                json.dump({}, f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
