# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 480)
        MainWindow.setMinimumSize(QtCore.QSize(320, 480))
        MainWindow.setMaximumSize(QtCore.QSize(320, 480))
        MainWindow.setBaseSize(QtCore.QSize(320, 480))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(320, 480))
        self.centralWidget.setMaximumSize(QtCore.QSize(320, 480))
        self.centralWidget.setBaseSize(QtCore.QSize(320, 480))
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 399, 301, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPreview = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnPreview.setObjectName("btnPreview")
        self.horizontalLayout.addWidget(self.btnPreview)
        self.btnSnap = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSnap.setObjectName("btnSnap")
        self.horizontalLayout.addWidget(self.btnSnap)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 301, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnSettings = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnSettings.setObjectName("btnSettings")
        self.horizontalLayout_2.addWidget(self.btnSettings)
        self.lblTeamName = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.lblTeamName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTeamName.setObjectName("lblTeamName")
        self.horizontalLayout_2.addWidget(self.lblTeamName)
        self.lblCamView = QtWidgets.QLabel(self.centralWidget)
        self.lblCamView.setGeometry(QtCore.QRect(0, 0, 320, 460))
        self.lblCamView.setMinimumSize(QtCore.QSize(320, 460))
        self.lblCamView.setMaximumSize(QtCore.QSize(320, 460))
        self.lblCamView.setBaseSize(QtCore.QSize(320, 460))
        self.lblCamView.setText("")
        self.lblCamView.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCamView.setObjectName("lblCamView")
        self.lblCamView.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPreview.setText(_translate("MainWindow", "Preview"))
        self.btnSnap.setText(_translate("MainWindow", "Snap"))
        self.btnSettings.setText(_translate("MainWindow", "Settings"))
        self.lblTeamName.setText(_translate("MainWindow", "Team Name"))

