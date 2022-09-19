# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_UI/interview_window.ui',
# licensing of 'interface_UI/interview_window.ui' applies.
#
# Created: Tue Jun 11 13:14:14 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

# Added from me:
import json
#


class Ui_InterviewWindow(object):

    def setupUi(self, InterviewWindow):
        InterviewWindow.setObjectName("InterviewWindow")
        InterviewWindow.resize(665, 413)
        self.centralwidget = QtWidgets.QWidget(InterviewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.options_widget_answer = QtWidgets.QWidget(self.centralwidget)
        self.options_widget_answer.setObjectName("options_widget_answer")
        self.verticalLayout_2.addWidget(self.options_widget_answer)
        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_buttons.setSizeConstraint(
            QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")
        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.horizontalLayout_buttons.addWidget(self.pushButton_menu)
        spacerItem4 = QtWidgets.QSpacerItem(
            268, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_buttons.addItem(spacerItem4)
        self.pushButton_previous = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.horizontalLayout_buttons.addWidget(self.pushButton_previous)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_buttons.addItem(spacerItem5)
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout_buttons.addWidget(self.pushButton_next)

        self.pushButton_finish = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.horizontalLayout_buttons.addWidget(self.pushButton_finish)

        self.verticalLayout_2.addLayout(self.horizontalLayout_buttons)
        InterviewWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InterviewWindow)
        QtCore.QMetaObject.connectSlotsByName(InterviewWindow)

        self.init_interview()

    def retranslateUi(self, InterviewWindow):
        InterviewWindow.setWindowTitle(QtWidgets.QApplication.translate(
            "InterviewWindow", "MainWindow", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate(
            "InterviewWindow", "1 of 13", None, -1))
        self.label.setText(QtWidgets.QApplication.translate(
            "InterviewWindow", "Question", None, -1))
        self.pushButton_menu.setText(QtWidgets.QApplication.translate(
            "InterviewWindow", "Menu", None, -1))
        self.pushButton_previous.setText(QtWidgets.QApplication.translate(
            "InterviewWindow", "Previous", None, -1))
        self.pushButton_next.setText(QtWidgets.QApplication.translate(
            "InterviewWindow", "Next", None, -1))
        self.pushButton_finish.setText(QtWidgets.QApplication.translate(
            "InterviewWindow", "Finish", None, -1))

#added from me

    def init_interview(self):
        self.names_questions = []
        self.added_elements = {}
        self.added_widgets = []
        self.verticalLayout_question_attr = QtWidgets.QVBoxLayout(
            self.options_widget_answer)
        self.nr_question = 0
        self.previous_nr_question = 0
        self.pushButton_finish.hide()


    def load_questions_json(self, path):
        with open(path, "r") as questions_json:
            self.questions = json.load(questions_json)
        self.add_question_attributes()
        self.update_question()


    def next_question(self):
        if self.nr_question + 1 < len(self.questions):
            self.previous_nr_question = self.nr_question
            self.nr_question += 1
            self.update_question()
            if self.nr_question == len(self.questions) - 1:
                self.pushButton_next.hide()
                self.pushButton_finish.show()


    def previous_question(self):
        if self.nr_question - 1 >= 0:
            self.previous_nr_question = self.nr_question
            self.nr_question -= 1
            self.update_question()
            if self.nr_question == len(self.questions) - 2:
                self.pushButton_next.show()
                self.pushButton_finish.hide()


    def update_question(self):
        self.label_2.setText(str(self.nr_question + 1) +
                             ' of ' + str(len(self.questions)))
        self.label.setText(
            self.questions[self.names_questions[self.nr_question]]["question"])

        for widget in self.added_elements[self.names_questions[self.previous_nr_question]]:
            widget['widget'].hide()

        for widget in self.added_elements[self.names_questions[self.nr_question]]:
            widget['widget'].show()


    def add_question_attributes(self):
        for name_question in self.questions:
            self.names_questions.append(name_question)
            self.added_elements[name_question] = []

            for field_name in self.questions[name_question]["field_type"]:
                if field_name == "int":
                    self.add_int_field(self.questions[name_question]["field_type"][field_name], name_question)
                elif field_name == "radio":
                    self.add_radio_field(self.questions[name_question]["field_type"][field_name], name_question)
                elif field_name == "float":
                    self.add_float_field(self.questions[name_question]["field_type"][field_name], name_question)

            for widget in self.added_elements[name_question]:
                widget['widget'].hide()
                self.verticalLayout_question_attr.addWidget(widget['widget'])


    def add_radio_field(self, attr, name_question):
        widget_container = {
            'widget': QtWidgets.QWidget(self.options_widget_answer),
            'widget_list': []
        }
        widget_container['layout'] = QtWidgets.QVBoxLayout(
            widget_container['widget'])

        for radio in attr:
            radio_button = {
                'widget': QtWidgets.QRadioButton(widget_container['widget']),
                'value': radio['value']
            }
            radio_button['widget'].setText(radio['text'])

            if len(widget_container['widget_list']) < 1:
                radio_button['widget'].setChecked(True)

            widget_container['widget_list'].append(radio_button)
            widget_container['layout'].addWidget(
                widget_container['widget_list'][-1]['widget'])

        self.added_elements[name_question].append(widget_container)


    def add_int_field(self, attr, name_question):
        spin_box = {
            'widget': QtWidgets.QSpinBox(self.options_widget_answer)
        }
        spin_box['widget'].setMaximum(999)
        self.added_elements[name_question].append(spin_box)


    def add_float_field(self, attr, name_question):
        double_spin_box = {
            'widget': QtWidgets.QDoubleSpinBox(self.options_widget_answer)
        }
        double_spin_box['widget'].setMaximum(999.0)
        self.added_elements[name_question].append(double_spin_box)


    def finish_interview(self):
        finish_data = []
        for name_question in self.names_questions:
            for widget in self.added_elements[name_question]:
                if type(widget['widget']) is QtWidgets.QWidget:
                    result = 0
                    for w_radio in widget['widget_list']:
                        if w_radio['widget'].isChecked():
                            result = w_radio['value']
                            break
                    
                    finish_data.append(result)
                else:
                    finish_data.append(widget['widget'].value())
        print(finish_data)
        return finish_data
