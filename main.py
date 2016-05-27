# always seem to need this
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# This is our window from QtCreator
import mainwindow_auto

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
# access variables inside of the UI's file
	def pressedPreviewButton(self):
		print("Pressed Preview!")
		myPixmap = QPixmap('/Users/russ_davis/Sites/picam/img/Rosie_IPA.png')
		myScaledPixmap = myPixmap.scaled(self.lblCamView.size(), Qt.KeepAspectRatio)
		self.lblCamView.setPixmap(myScaledPixmap)

	def pressedSnapButton(self):
		print("Pressed Snap")
		self.lblCamView.clear()

	def pressedSettingsButton(self):
		print("Settings pressed")


	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) # gets defined in the UI file


		# Tie buttons to clicks
		self.btnSnap.clicked.connect(lambda: self.pressedSnapButton())
		self.btnPreview.clicked.connect(lambda: self.pressedPreviewButton())
		self.btnSettings.clicked.connect(lambda: self.pressedSetingsButton())


def main():
	# a new app instance
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	# without this, the script exits immediately.
	sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
	main()