# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FINAL_FINAL.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pyqt(object):
    def setupUi(self, Pyqt):
        Pyqt.setObjectName("Pyqt")
        Pyqt.resize(644, 562)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Pyqt.setFont(font)
        Pyqt.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Pyqt)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.TEXT_BOX = QtWidgets.QTextBrowser(self.centralwidget)
        self.TEXT_BOX.setObjectName("TEXT_BOX")
        self.gridLayout.addWidget(self.TEXT_BOX, 0, 0, 1, 5)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.BROWSE = QtWidgets.QPushButton(self.centralwidget)
        self.BROWSE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BROWSE.setMouseTracking(False)
        self.BROWSE.setObjectName("BROWSE")
        self.gridLayout.addWidget(self.BROWSE, 1, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 1, 1, 4)
        self.Download = QtWidgets.QPushButton(self.centralwidget)
        self.Download.setObjectName("Download")
        self.gridLayout.addWidget(self.Download, 4, 1, 1, 4)
        Pyqt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Pyqt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 26))
        self.menubar.setObjectName("menubar")
        Pyqt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Pyqt)
        self.statusbar.setObjectName("statusbar")
        Pyqt.setStatusBar(self.statusbar)

        self.retranslateUi(Pyqt)
        QtCore.QMetaObject.connectSlotsByName(Pyqt)

    def retranslateUi(self, Pyqt):
        _translate = QtCore.QCoreApplication.translate
        Pyqt.setWindowTitle(_translate("Pyqt", "MainWindow"))
        self.TEXT_BOX.setHtml(_translate("Pyqt", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#0400f7;\">IMAGE PROCESSING WITH</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:400; color:#983d08;\">TESSERACT OCR </span></p></body></html>"))
        self.BROWSE.setText(_translate("Pyqt", "SELECT IMAGE"))
        self.pushButton.setText(_translate("Pyqt", "Process"))
        self.label_2.setText(_translate("Pyqt", "Select Language"))
        self.radioButton.setText(_translate("Pyqt", "ENGLISH"))
        self.radioButton_2.setText(_translate("Pyqt", "GUJARAT"))
        self.label.setText(_translate("Pyqt", "OUTPUT :"))
        self.Download.setText(_translate("Pyqt", "DOWNLOAD"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pyqt = QtWidgets.QMainWindow()
    ui = Ui_Pyqt()
    ui.setupUi(Pyqt)
    Pyqt.show()
    sys.exit(app.exec_())
