# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Sun Jun  2 17:54:57 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.question = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Bamum")
        font.setPointSize(16)
        font.setWeight(50)
        font.setBold(False)
        self.question.setFont(font)
        self.question.setObjectName("question")
        self.verticalLayout_2.addWidget(self.question)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_classfifier = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_classfifier.setEnabled(True)
        self.radioButton_classfifier.setChecked(True)
        self.radioButton_classfifier.setAutoExclusive(True)
        self.radioButton_classfifier.setObjectName("radioButton_classfifier")
        self.verticalLayout.addWidget(self.radioButton_classfifier)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.line.setFont(font)
        self.line.setMouseTracking(False)
        self.line.setAutoFillBackground(True)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout_2.addWidget(self.pushButton_start)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.question.setText(QtWidgets.QApplication.translate("MainWindow", "What method do you want to choose?", None, -1))
        self.radioButton_classfifier.setText(QtWidgets.QApplication.translate("MainWindow", "Classifier", None, -1))
        self.pushButton_start.setText(QtWidgets.QApplication.translate("MainWindow", "Get started", None, -1))

