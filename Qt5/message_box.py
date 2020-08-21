# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message_box.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(230, 200, 321, 141))
        self.button1.setObjectName("button1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #my modification
        self.button1.clicked.connect(self.show_popup)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "PushButton"))

    #my modification
    def show_popup(self):
        msg = QMessageBox() # has to be imported first. messagebox appears when button is clicked.
        msg.setWindowTitle('Hier könnte Ihre Werbung stehen')
        msg.setText('Hello my name Buddy and you can me, anytime!')

        #set icon
        msg.setIcon(QMessageBox.Information)
        #msg.setIcon(QMessageBox.Critical)
        #msg.setIcon(QMessageBox.Question)
        #msg.setIcon(QMessageBox.Warning)

        #button specifications
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Abort|QMessageBox.Ok|QMessageBox.Retry)
        msg.setDefaultButton(QMessageBox.Ok)
        
        #informative text
        msg.setInformativeText('informartive test!')

        #detail text
        msg.setDetailedText('details')

        #to see in the terminal which button was clicked
        msg.buttonClicked.connect(self.button_pressed)

        x = msg.exec_() # executes the message box --> shows it.

    #method to show which button is clicked
    def button_pressed(self,i):
        print(i.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

