#!./venv/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from interface.main_window import Ui_MainWindow
from interface.interview_window import Ui_InterviewWindow
from interface.result_window import Ui_ResultMenu

from decision_tree import DecisionTree
from saver_results import SaveResult

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.nr_question = 0
        self.interview_data = []
        self.classifier = False
        self.regression = False
        self.ui = None
        self.go_to_main_window()
        self.d_tree = DecisionTree(max_depth=6)
        path_to_dataset = os.path.join('dataset', 'joint_dataset.data')
        self.path_to_questions_json = os.path.join("questions", "questions.json")
        self.d_tree.load_dataset(path_to_dataset)

    def go_to_main_window(self):
        self.reset_data()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_start.clicked.connect(self.check_preferences)

    def reset_data(self):
        self.nr_question = 0
        self.interview_data = []
        self.classifier = False

    def check_preferences(self):
        if self.ui.radioButton_classfifier.isChecked():
            self.classifier = True
            self.d_tree.training_classifier()

        self.go_to_interview()

    def go_to_interview(self):
        self.ui = Ui_InterviewWindow()        
        self.ui.setupUi(self)
        self.ui.load_questions_json(self.path_to_questions_json)
        self.ui.pushButton_next.clicked.connect(self.next_question)
        self.ui.pushButton_finish.clicked.connect(self.go_to_result)
        self.ui.pushButton_previous.clicked.connect(self.previous_question)

    def next_question(self):
        self.ui.next_question()

    def previous_question(self):
        self.ui.previous_question()
        
    def save_results(self, data):
        save_res = SaveResult()
        save_res.set_path("dataset/new_results.data")
        save_res.save(data)
        
    def go_to_result(self):
        data_to_analysis = self.ui.finish_interview()
        if self.classifier:
            result = self.d_tree.predict_by_classification([data_to_analysis])
            
        self.save_results(data_to_analysis + result)
            
        self.ui = Ui_ResultMenu()
        self.ui.setupUi(self)
        self.ui.result_text(result[0])
        
        self.ui.pushButton_menu.clicked.connect(self.go_to_main_window)
        self.ui.pushButton_exit.clicked.connect(self.close)      
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
