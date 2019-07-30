# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Loginform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(588, 523)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 180, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Login_Username = QtWidgets.QLineEdit(Dialog)
        self.Login_Username.setGeometry(QtCore.QRect(210, 190, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Login_Username.setFont(font)
        self.Login_Username.setObjectName("Login_Username")
        self.CreateAcc = QtWidgets.QPushButton(Dialog)
        self.CreateAcc.setGeometry(QtCore.QRect(90, 430, 141, 41))
        self.CreateAcc.setObjectName("CreateAcc")
        self.NextToPass = QtWidgets.QPushButton(Dialog)
        self.NextToPass.setGeometry(QtCore.QRect(240, 260, 171, 61))
        self.NextToPass.setObjectName("NextToPass")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 400, 251, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Username"))
        self.CreateAcc.setText(_translate("Dialog", "Register"))
        self.NextToPass.setText(_translate("Dialog", "Next"))
        self.label_2.setText(_translate("Dialog", "Don\'t have an account? Register now!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

