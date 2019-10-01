# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from anup import *

class Ui_loginwindow(object):
    switch_window = QtCore.pyqtSignal()

    def setupUi(self, loginwindow):
        loginwindow.setObjectName("loginwindow")
        loginwindow.resize(555, 518)
        loginwindow.setStyleSheet("background-image: url(:/ak/46356490-food-delivery-design-vector-illustration-eps10-graphic.jpg);")
        self.centralwidget = QtWidgets.QWidget(loginwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 231, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.loginid = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.loginid.setFont(font)
        self.loginid.setMaxLength(32)
        self.loginid.setObjectName("loginid")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginid)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.password = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setMaxLength(32)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.reset = QtWidgets.QPushButton(self.formLayoutWidget)
        self.reset.setObjectName("reset")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.reset)
        self.go = QtWidgets.QPushButton(self.formLayoutWidget)
        self.go.setObjectName("go")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.go)
        self.newsign = QtWidgets.QPushButton(self.formLayoutWidget)
        self.newsign.setObjectName("newsign")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.newsign)
        loginwindow.setCentralWidget(self.centralwidget)
        self.cd = QtWidgets.QAction(loginwindow)
        self.cd.setObjectName("cd")
        self.rab = QtWidgets.QAction(loginwindow)
        self.rab.setObjectName("rab")

        self.retranslateUi(loginwindow)
        self.reset.clicked.connect(self.password.clear)
        self.reset.clicked.connect(self.loginid.clear)
        QtCore.QMetaObject.connectSlotsByName(loginwindow)

    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("loginwindow", "LOGIN"))
        self.label_2.setText(_translate("loginwindow", "LOGIN ID"))
        self.label_3.setText(_translate("loginwindow", "PASSWORD"))
        self.reset.setText(_translate("loginwindow", "RESET"))
        self.go.setText(_translate("loginwindow", "GO"))
        self.newsign.setText(_translate("loginwindow", "NEW SIGN UP"))
        self.cd.setText(_translate("loginwindow", "Contact Developer"))
        self.rab.setText(_translate("loginwindow", "Report A Bug"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginwindow = QtWidgets.QMainWindow()
    ui = Ui_loginwindow()
    ui.setupUi(loginwindow)
    loginwindow.show()
    sys.exit(app.exec_())

