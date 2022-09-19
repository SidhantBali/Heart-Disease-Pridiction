# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result_window.ui',
# licensing of 'result_window.ui' applies.
#
# Created: Sun Jun  2 18:52:27 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ResultMenu(object):
    def setupUi(self, ResultMenu):
        ResultMenu.setObjectName("ResultMenu")
        ResultMenu.resize(681, 474)
        self.centralwidget = QtWidgets.QWidget(ResultMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")
        self.horizontalLayout_2.addWidget(self.result_label)
        spacerItem4 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.horizontalLayout_3.addWidget(self.pushButton_menu)
        spacerItem6 = QtWidgets.QSpacerItem(438, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_3.addWidget(self.pushButton_exit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        ResultMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(ResultMenu)
        QtCore.QMetaObject.connectSlotsByName(ResultMenu)
        ResultMenu.setTabOrder(self.pushButton_menu, self.pushButton_exit)

    def retranslateUi(self, ResultMenu):
        ResultMenu.setWindowTitle(QtWidgets.QApplication.translate("ResultMenu", "Result", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ResultMenu", "0 - no deviation detected", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ResultMenu", "1 - 4 is a deviation level", None, -1))
        self.result_label.setText(QtWidgets.QApplication.translate("ResultMenu", "1", None, -1))
        self.pushButton_menu.setText(QtWidgets.QApplication.translate("ResultMenu", "Menu", None, -1))
        self.pushButton_exit.setText(QtWidgets.QApplication.translate("ResultMenu", "Exit", None, -1))
        
#added from me:

    def result_text(self, result):
        if result == 0:
            result_text = "<font color='green'>Heart disease not detected</font>"
        elif result == 1:
            result_text = "<font color='red'>Heart disease detected</font>"
        elif result == 2:  
            result_text = "<font color='red'>Heart disease detected</font>"
        elif result == 3:
            result_text = "<font color='red'>Heart disease detected</font>"
        elif result == 4:
            result_text = "<font color='red'>Heart disease detected</font>"
        self.result_label.setText(result_text)

