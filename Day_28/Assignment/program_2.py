# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'program2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_mohit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_mohit.setGeometry(QtCore.QRect(40, 30, 461, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textEdit_mohit.setFont(font)
        self.textEdit_mohit.setObjectName("textEdit_mohit")
        self.lineEdit_mohit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_mohit.setGeometry(QtCore.QRect(40, 290, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_mohit.setFont(font)
        self.lineEdit_mohit.setObjectName("lineEdit_mohit")
        self.QCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.QCheckBox.setGeometry(QtCore.QRect(140, 200, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QCheckBox.setFont(font)
        self.QCheckBox.setObjectName("QCheckBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.QCheckBox.setText(_translate("MainWindow", "Click to copy Paste"))
        self.QCheckBox.toggled.connect(self.copy)

    def copy(self):
        data = self.textEdit_mohit.toPlainText()
        self.lineEdit_mohit.setText(data)
        self.QCheckBox.setText("Clicked pasted")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
