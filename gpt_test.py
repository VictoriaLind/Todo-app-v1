from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication([])

# create a QWidget as the main window
main_window = QtWidgets.QWidget()

# create a QVBoxLayout and add it to the main window
vbox = QtWidgets.QVBoxLayout()
main_window.setLayout(vbox)

# create a QLabel widget and add it to the layout
label = QtWidgets.QLabel("Hello, World!")
vbox.addWidget(label)

# set the alignment of the label to top
vbox.setAlignment(label, QtCore.Qt.AlignTop)

main_window.show()

app.exec_()
