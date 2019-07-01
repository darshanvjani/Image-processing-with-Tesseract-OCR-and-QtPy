import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from PyQt5 import QtWidgets,QtCore,uic
from PIL import Image
import pytesseract

import final_ui

class MyWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self,parent)
		self.ui = final_ui.Ui_Pyqt()
		self.ui.setupUi(self)
		self.ui.BROWSE.clicked.connect(self.getfiles)
		self.ui.pushButton.clicked.connect(self.ocr)
		self.ui.Download.clicked.connect(self.download)
	def getfiles(self):
		fileName = str((QtWidgets.QFileDialog.getOpenFileName(self, "Select file"))[0])
		self.ui.lineEdit.setText(fileName)
	def ocr(self):
		path=self.ui.lineEdit.text()
		print(path)
		if self.ui.radioButton.isChecked()==True:
			im = Image.open(path)
			text= pytesseract.image_to_string(im,lang="eng")
			self.ui.textEdit.setText(text)
		else:
			im = Image.open(path)
			text= pytesseract.image_to_string(im,lang="guj")
			self.ui.textEdit.setText(text)
		return text
	def download(self):
		w=open('D:\\project\\IMAGE_TO_TEXT.txt','w',encoding='utf-8')
		a=self.ocr()
		w.write(a)
		w.close()
		
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


