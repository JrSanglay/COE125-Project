from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtTest
import sqlite3
import io

class Ui_ExamWindow(object):
    def setupUi(self, ExamWindow, Name):
        ExamWindow.setObjectName("ExamWindow")
        ExamWindow.resize(478, 292)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        ExamWindow.setPalette(palette)
        self.Label_Note = QtWidgets.QLabel(ExamWindow)
        self.Label_Note.setGeometry(QtCore.QRect(330, 210, 141, 71))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Note.setFont(font)
        self.Label_Note.setObjectName("Label_Note")
        self.pushButton_GenQues = QtWidgets.QPushButton(ExamWindow)
        self.pushButton_GenQues.setGeometry(QtCore.QRect(10, 260, 121, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_GenQues.setFont(font)
        self.pushButton_GenQues.setObjectName("pushButton_GenQues")
        self.Label_Picture = QtWidgets.QLabel(ExamWindow)
        self.Label_Picture.setGeometry(QtCore.QRect(140, 60, 171, 121))
        self.Label_Picture.setObjectName("Label_Picture")
        self.Label_WhatIs = QtWidgets.QLabel(ExamWindow)
        self.Label_WhatIs.setGeometry(QtCore.QRect(130, 190, 191, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_WhatIs.setFont(font)
        self.Label_WhatIs.setObjectName("Label_WhatIs")
        self.lineEdit_Answer = QtWidgets.QLineEdit(ExamWindow)
        self.lineEdit_Answer.setGeometry(QtCore.QRect(130, 220, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Answer.setFont(font)
        self.lineEdit_Answer.setObjectName("lineEdit_Answer")
        self.pushButton_ShowAnswers = QtWidgets.QPushButton(ExamWindow)
        self.pushButton_ShowAnswers.setGeometry(QtCore.QRect(330, 70, 141, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ShowAnswers.setFont(font)
        self.pushButton_ShowAnswers.setObjectName("pushButton_ShowAnswers")
        self.Label_Score = QtWidgets.QLabel(ExamWindow)
        self.Label_Score.setGeometry(QtCore.QRect(340, 40, 41, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Score.setFont(font)
        self.Label_Score.setObjectName("Label_Score")
        self.Label_ScoreCurrent = QtWidgets.QLabel(ExamWindow)
        self.Label_ScoreCurrent.setGeometry(QtCore.QRect(390, 40, 16, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_ScoreCurrent.setFont(font)
        self.Label_ScoreCurrent.setObjectName("Label_ScoreCurrent")
        self.Label_ScoreMax = QtWidgets.QLabel(ExamWindow)
        self.Label_ScoreMax.setGeometry(QtCore.QRect(400, 40, 16, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_ScoreMax.setFont(font)
        self.Label_ScoreMax.setObjectName("Label_ScoreMax")
        self.Label_Question1Ans = QtWidgets.QLabel(ExamWindow)
        self.Label_Question1Ans.setGeometry(QtCore.QRect(330, 100, 191, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Question1Ans.setFont(font)
        self.Label_Question1Ans.setObjectName("Label_Question1Ans")
        self.Label_Question2Ans = QtWidgets.QLabel(ExamWindow)
        self.Label_Question2Ans.setGeometry(QtCore.QRect(330, 120, 191, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Question2Ans.setFont(font)
        self.Label_Question2Ans.setObjectName("Label_Question2Ans")
        self.Label_Question4Ans = QtWidgets.QLabel(ExamWindow)
        self.Label_Question4Ans.setGeometry(QtCore.QRect(330, 160, 191, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Question4Ans.setFont(font)
        self.Label_Question4Ans.setObjectName("Label_Question4Ans")
        self.Label_Question3Ans = QtWidgets.QLabel(ExamWindow)
        self.Label_Question3Ans.setGeometry(QtCore.QRect(330, 140, 191, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Question3Ans.setFont(font)
        self.Label_Question3Ans.setObjectName("Label_Question3Ans")
        self.Label_Question5Ans = QtWidgets.QLabel(ExamWindow)
        self.Label_Question5Ans.setGeometry(QtCore.QRect(330, 180, 191, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Question5Ans.setFont(font)
        self.Label_Question5Ans.setObjectName("Label_Question5Ans")
        self.pushButton_SubmitAnswer = QtWidgets.QPushButton(ExamWindow)
        self.pushButton_SubmitAnswer.setGeometry(QtCore.QRect(170, 250, 121, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SubmitAnswer.setFont(font)
        self.pushButton_SubmitAnswer.setObjectName("pushButton_SubmitAnswer")
        self.pushButton_SignOut = QtWidgets.QPushButton(ExamWindow)
        self.pushButton_SignOut.setGeometry(QtCore.QRect(410, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SignOut.setFont(font)
        self.pushButton_SignOut.setObjectName("pushButton_SignOut")
        self.Label_WelcomeUser = QtWidgets.QLabel(ExamWindow)
        self.Label_WelcomeUser.setGeometry(QtCore.QRect(10, 10, 271, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_WelcomeUser.setFont(font)
        self.Label_WelcomeUser.setObjectName("Label_WelcomeUser")
        self.Label_Question = QtWidgets.QLabel(ExamWindow)
        self.Label_Question.setGeometry(QtCore.QRect(10, 40, 71, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Question.setFont(font)
        self.Label_Question.setObjectName("Label_Question")
        self.Label_QuestionCurrent = QtWidgets.QLabel(ExamWindow)
        self.Label_QuestionCurrent.setGeometry(QtCore.QRect(80, 40, 16, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_QuestionCurrent.setFont(font)
        self.Label_QuestionCurrent.setObjectName("Label_QuestionCurrent")
        self.pushButton_AddFruit = QtWidgets.QPushButton(ExamWindow)
        self.pushButton_AddFruit.setGeometry(QtCore.QRect(10, 230, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_AddFruit.setFont(font)
        self.pushButton_AddFruit.setObjectName("pushButton_AddFruit")
        self.Label_QuizStatus = QtWidgets.QLabel(ExamWindow)
        self.Label_QuizStatus.setGeometry(QtCore.QRect(140, 40, 181, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_QuizStatus.setFont(font)
        self.Label_QuizStatus.setObjectName("Label_QuizStatus")
        self.groupBox_Choices = QtWidgets.QGroupBox(ExamWindow)
        self.groupBox_Choices.setGeometry(QtCore.QRect(10, 70, 111, 151))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Choices.setFont(font)
        self.groupBox_Choices.setObjectName("groupBox_Choices")
        self.Label_ChoicesWatermelon = QtWidgets.QLabel(self.groupBox_Choices)
        self.Label_ChoicesWatermelon.setGeometry(QtCore.QRect(10, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_ChoicesWatermelon.setFont(font)
        self.Label_ChoicesWatermelon.setObjectName("Label_ChoicesWatermelon")
        self.Label_ChoicesBanana = QtWidgets.QLabel(self.groupBox_Choices)
        self.Label_ChoicesBanana.setGeometry(QtCore.QRect(10, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_ChoicesBanana.setFont(font)
        self.Label_ChoicesBanana.setObjectName("Label_ChoicesBanana")
        self.Label_ChoicesGrape = QtWidgets.QLabel(self.groupBox_Choices)
        self.Label_ChoicesGrape.setGeometry(QtCore.QRect(10, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_ChoicesGrape.setFont(font)
        self.Label_ChoicesGrape.setObjectName("Label_ChoicesGrape")
        self.Label_ChoicesMango = QtWidgets.QLabel(self.groupBox_Choices)
        self.Label_ChoicesMango.setGeometry(QtCore.QRect(10, 100, 61, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_ChoicesMango.setFont(font)
        self.Label_ChoicesMango.setObjectName("Label_ChoicesMango")
        self.Label_ChoicesOrange = QtWidgets.QLabel(self.groupBox_Choices)
        self.Label_ChoicesOrange.setGeometry(QtCore.QRect(10, 80, 61, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_ChoicesOrange.setFont(font)
        self.Label_ChoicesOrange.setObjectName("Label_ChoicesOrange")
        self.Label_ChoicesApple = QtWidgets.QLabel(self.groupBox_Choices)
        self.Label_ChoicesApple.setGeometry(QtCore.QRect(10, 40, 61, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_ChoicesApple.setFont(font)
        self.Label_ChoicesApple.setObjectName("Label_ChoicesApple")
        self.Label_ChoicesWatermelon.raise_()
        self.Label_ChoicesBanana.raise_()
        self.Label_ChoicesGrape.raise_()
        self.Label_ChoicesMango.raise_()
        self.Label_ChoicesOrange.raise_()
        self.Label_ChoicesApple.raise_()
        
        self.pushButton_GenQues.clicked.connect(self.StartQuiz)
        self.pushButton_SubmitAnswer.clicked.connect(self.SubmitAnswer)
        self.pushButton_ShowAnswers.clicked.connect(self.ShowAnswers)
        self.pushButton_SignOut.clicked.connect(self.SignOut)
        
        self.retranslateUi(ExamWindow)
        
        self.Label_WelcomeUser.setText("Welcome " + Name + "!")
        
        QtCore.QMetaObject.connectSlotsByName(ExamWindow)
        ExamWindow.setTabOrder(self.pushButton_SignOut, self.pushButton_GenQues)
        ExamWindow.setTabOrder(self.pushButton_GenQues, self.pushButton_AddFruit)
        ExamWindow.setTabOrder(self.pushButton_AddFruit, self.lineEdit_Answer)
        ExamWindow.setTabOrder(self.lineEdit_Answer, self.pushButton_SubmitAnswer)
        ExamWindow.setTabOrder(self.pushButton_SubmitAnswer, self.pushButton_ShowAnswers)

    def retranslateUi(self, ExamWindow):
        _translate = QtCore.QCoreApplication.translate
        ExamWindow.setWindowTitle(_translate("ExamWindow", "Exam"))
        self.Label_Note.setText(_translate("ExamWindow", "<html><head/><body><p>Note:</p><p>The Exam Consists </p><p>Of Only 5 Questions.</p></body></html>"))
        self.pushButton_GenQues.setText(_translate("ExamWindow", "Generate Questions"))
        self.Label_Picture.setText(_translate("ExamWindow", "LAGYANAN NG PICTURE"))
        self.Label_WhatIs.setText(_translate("ExamWindow", "What is the name of the fruit?"))
        self.pushButton_ShowAnswers.setText(_translate("ExamWindow", "Show Correct/Incorrect"))
        self.Label_Score.setText(_translate("ExamWindow", "Score:"))
        self.Label_ScoreCurrent.setText(_translate("ExamWindow", "0"))
        self.Label_ScoreMax.setText(_translate("ExamWindow", "/ 5"))
        self.Label_Question1Ans.setText(_translate("ExamWindow", "Question 1: "))
        self.Label_Question2Ans.setText(_translate("ExamWindow", "Question 2: "))
        self.Label_Question4Ans.setText(_translate("ExamWindow", "Question 4: "))
        self.Label_Question3Ans.setText(_translate("ExamWindow", "Question 3: "))
        self.Label_Question5Ans.setText(_translate("ExamWindow", "Question 5: "))
        self.pushButton_SubmitAnswer.setText(_translate("ExamWindow", "Submit Answer"))
        self.pushButton_SignOut.setText(_translate("ExamWindow", "Sign Out"))
        self.Label_WelcomeUser.setText(_translate("ExamWindow", "Welcome, FIRSTNAME LASTNAME!"))
        self.Label_Question.setText(_translate("ExamWindow", "Question #"))
        self.Label_QuestionCurrent.setText(_translate("ExamWindow", "#"))
        self.pushButton_AddFruit.setText(_translate("ExamWindow", "Add Fruit Image"))
        self.Label_QuizStatus.setText(_translate("ExamWindow", "Nothing Going On..."))
        self.groupBox_Choices.setTitle(_translate("ExamWindow", "Choices:"))
        self.Label_ChoicesWatermelon.setText(_translate("ExamWindow", "Watermelon"))
        self.Label_ChoicesBanana.setText(_translate("ExamWindow", "Banana"))
        self.Label_ChoicesGrape.setText(_translate("ExamWindow", "Grape"))
        self.Label_ChoicesMango.setText(_translate("ExamWindow", "Mango"))
        self.Label_ChoicesOrange.setText(_translate("ExamWindow", "Orange"))
        self.Label_ChoicesApple.setText(_translate("ExamWindow", "Apple"))

        self.Label_ChoicesWatermelon.setStyleSheet("color: blue;")
        self.Label_ChoicesBanana.setStyleSheet("color: blue;")
        self.Label_ChoicesGrape.setStyleSheet("color: blue;")
        self.Label_ChoicesMango.setStyleSheet("color: blue;")
        self.Label_ChoicesOrange.setStyleSheet("color: blue;")
        self.Label_ChoicesApple.setStyleSheet("color: blue;")
        
        self.Label_QuizStatus.setStyleSheet("color: blue;")

        self.Label_Note.hide()
        self.Label_Picture.hide()
        
        self.Label_QuestionCurrent.hide()
        
        self.Label_Question1Ans.hide()
        self.Label_Question2Ans.hide()
        self.Label_Question3Ans.hide()
        self.Label_Question4Ans.hide()
        self.Label_Question5Ans.hide()
        
        self.Label_Score.hide()
        self.Label_ScoreCurrent.hide()
        self.Label_ScoreMax.hide()
        self.Label_WhatIs.hide()
        
        self.pushButton_ShowAnswers.hide()
        self.lineEdit_Answer.setEnabled(False)
        self.pushButton_SubmitAnswer.setEnabled(False)





    def StartQuiz(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        m = cursor.execute("""
        SELECT * FROM Images ORDER BY RANDOM () LIMIT 1;
        """)
        for x in m:
            rec_data = x[1]
        with open ('fruit.png', 'wb') as f:
            f.write(rec_data)
        self.Label_Picture.show()
        self.Label_Picture.setPicture('Grape.png')


        self.Label_QuizStatus.setText("Quiz Started!")
        self.Label_QuizStatus.setStyleSheet("color: green;")

        
        self.pushButton_SubmitAnswer.show()
        self.pushButton_SubmitAnswer.setEnabled(True)
    
        self.Label_WhatIs.show()
        self.lineEdit_Answer.show()
        self.lineEdit_Answer.setEnabled(True)
        
        self.Label_QuestionCurrent.show()
        self.Label_QuestionCurrent.setText("1")
        
        self.Label_Question1Ans.hide()
        self.Label_Question2Ans.hide()
        self.Label_Question3Ans.hide()
        self.Label_Question4Ans.hide()
        self.Label_Question5Ans.hide()
        self.pushButton_ShowAnswers.hide()
        self.pushButton_ShowAnswers.setText("Show Correct/Incorrect")
        self.pushButton_GenQues.setEnabled(False)
        self.pushButton_AddFruit.setEnabled(False)
        
        self.Label_Score.hide()
        self.Label_ScoreCurrent.hide()
        self.Label_ScoreMax.hide()
        
        self.pushButton_SignOut.setEnabled(False)

        
    def SubmitAnswer(self):
        Answer = self.lineEdit_Answer.text()
        
        if Answer == "":
            self.Label_QuizStatus.setText("Your answer is blank!")
            self.Label_QuizStatus.setStyleSheet("color: red;")
            
        elif Answer == "Banana" or Answer == "Apple" or Answer == "Grape" or Answer == "Orange" or Answer == "Mango" or Answer == "Watermelon":
            if self.Label_QuestionCurrent.text() >= "5":      
                self.Label_Score.show()
                self.Label_ScoreCurrent.show()
                self.Label_ScoreMax.show()
                self.pushButton_ShowAnswers.show()
                self.Label_QuizStatus.setText("Quiz Completed!")
                self.Label_QuizStatus.setStyleSheet("color: green;")
                self.pushButton_GenQues.setEnabled(True)
                self.pushButton_AddFruit.setEnabled(True)
                self.lineEdit_Answer.setEnabled(False)
                self.pushButton_SubmitAnswer.setEnabled(False)
                self.Label_WhatIs.hide()
                self.Label_Picture.hide()
                
                self.Label_QuestionCurrent.hide()
                
                self.pushButton_SignOut.setEnabled(True)

                
            else:
                Num = int(self.Label_QuestionCurrent.text())
                Num = Num + 1
                self.Label_QuestionCurrent.setText(str(Num))
                self.Label_QuizStatus.setText("Next Question!")
                self.Label_QuizStatus.setStyleSheet("color: blue;")
            
        else:
            self.Label_QuizStatus.setText("Follow only the choices!")
            self.Label_QuizStatus.setStyleSheet("color: red;")
        
        self.lineEdit_Answer.setText("")

    def ShowAnswers(self):
        if self.pushButton_ShowAnswers.text() == "Show Correct/Incorrect":
            self.pushButton_ShowAnswers.setText("Hide Correct/Incorrect")
            self.Label_Question1Ans.show()
            self.Label_Question2Ans.show()
            self.Label_Question3Ans.show()
            self.Label_Question4Ans.show()
            self.Label_Question5Ans.show()
        
        elif self.pushButton_ShowAnswers.text() == "Hide Correct/Incorrect":
            self.pushButton_ShowAnswers.setText("Show Correct/Incorrect")
            self.Label_Question1Ans.hide()
            self.Label_Question2Ans.hide()
            self.Label_Question3Ans.hide()
            self.Label_Question4Ans.hide()
            self.Label_Question5Ans.hide()
    
    def SignOut(self):
        self.Label_QuizStatus.setText("Signing Out...")
        self.Label_QuizStatus.setStyleSheet("color: blue;")
        QtTest.QTest.qWait(3000)

        ExamWindow.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExamWindow = QtWidgets.QDialog()
    ui = Ui_ExamWindow()
    ui.setupUi(ExamWindow,Name=('Joshua'))
    ExamWindow.show()
    sys.exit(app.exec_())

































