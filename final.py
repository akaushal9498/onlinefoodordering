import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import mysql.connector

mydb = mysql.connector.connect(
    host="Localhost",
    user="root",
    passwd="asdfghjkl",
    database="login")
mycursor= mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS id(uname VARCHAR(40),passwd VARCHAR(32))")
mydb.commit()

class firstwindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.le1 = QtWidgets.QLineEdit()
        self.le2 = QtWidgets.QLineEdit()
        self.lb = QtWidgets.QLabel("USERNAME")
        self.lb2 = QtWidgets.QLabel("PASSWORD")
        self.pb = QtWidgets.QPushButton("OK")
        self.pb2 = QtWidgets.QPushButton("RESET")
        self.pb3 = QtWidgets.QPushButton("NEW SIGNUP")
        self.le2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le2.setMaxLength(32)
        self.le1.setMaxLength(32)
        self.pb2.clicked.connect(self.le1.clear)
        self.pb2.clicked.connect(self.le2.clear)
        self.pb3.clicked.connect(self.switch)
        self.pb.clicked.connect(self.switch2)

        fbox1 = QtWidgets.QVBoxLayout()
        fbox1.addWidget(self.lb)
        fbox1.addWidget(self.le1)
        fbox1.addWidget(self.lb2)
        fbox1.addWidget(self.le2)
        fbox1.addWidget(self.pb)
        fbox1.addWidget(self.pb2)
        fbox1.addWidget(self.pb3)
        self.setLayout(fbox1)
        self.setFixedSize(600,400)

        self.setWindowTitle("FOOD DELIVERY")


    def switch(self):

        self.switch_window.emit()

    def switch2(self):
        self.switch_window2.emit()

class secondwindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui2()

    def init_ui2(self):
        self.le1 = QtWidgets.QLineEdit()
        self.le2 = QtWidgets.QTextEdit()
        self.le3 = QtWidgets.QLineEdit()
        self.le4 = QtWidgets.QLineEdit()
        self.le5 = QtWidgets.QLineEdit()
        self.lb = QtWidgets.QLabel("NAME")
        self.lb2 = QtWidgets.QLabel("ADDRESS")
        self.lb3 = QtWidgets.QLabel("MOBILE")
        self.lb4 = QtWidgets.QLabel("EMAIL")
        self.lb5 = QtWidgets.QLabel("PASSWORD")
        self.male = QtWidgets.QRadioButton("MALE")
        self.female = QtWidgets.QRadioButton("FEMALE")
        self.others = QtWidgets.QRadioButton("OTHERS")

        self.pb = QtWidgets.QPushButton("SIGN UP")
        self.pb2 = QtWidgets.QPushButton("RESET")
        self.pb3 = QtWidgets.QPushButton("BACK")
        self.pb2.clicked.connect(self.le1.clear)
        self.pb2.clicked.connect(self.le2.clear)
        self.pb2.clicked.connect(self.le3.clear)
        self.pb2.clicked.connect(self.le4.clear)
        self.pb2.clicked.connect(self.le5.clear)
        self.pb.clicked.connect(self.submit)
        self.pb.clicked.connect(self.switch)
        self.pb3.clicked.connect(self.switch)

        fbox1 = QtWidgets.QVBoxLayout()
        fbox1.addWidget(self.lb)
        fbox1.addWidget(self.le1)
        self.le1.setMaxLength(32)
        fbox1.addWidget(self.lb2)
        fbox1.addWidget(self.le2)
        fbox1.addWidget(self.lb3)
        fbox1.addWidget(self.le3)
        self.le3.setMaxLength(10)
        fbox1.addWidget(self.lb4)
        fbox1.addWidget(self.le4)
        self.le4.setMaxLength(40)
        fbox1.addWidget(self.lb5)
        fbox1.addWidget(self.le5)
        self.le5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le5.setMaxLength(32)
        fbox1.addWidget(self.male)
        fbox1.addWidget(self.female)
        fbox1.addWidget(self.others)
        fbox1.addWidget(self.pb)
        fbox1.addWidget(self.pb2)
        fbox1.addWidget(self.pb3)
        self.setLayout(fbox1)
        self.setFixedSize(600, 400)
        self.setWindowTitle("FOOD DELIVERY")

    def submit(self):
        uname = self.le4.text()
        passwd = self.le5.text()
        sqlquery = "INSERT INTO id VALUES(%s,%s)"
        user = (uname, passwd)
        mycursor.execute(sqlquery, user)
        mydb.commit()
    def switch(self):
        self.switch_window.emit()
        self.hide()

class thirdwindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui3()

    def init_ui3(self):
        self.pb = QtWidgets.QPushButton("NEW ORDER")
        self.pb2 = QtWidgets.QPushButton("ORDER HISTORY")
        self.pb3 = QtWidgets.QPushButton("LOGOUT")
        self.pb3.clicked.connect(self.switch)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.pb)
        vbox.addWidget(self.pb2)
        vbox.addWidget(self.pb3)
        self.setLayout(vbox)
        self.setFixedSize(600, 400)
        self.setWindowTitle("FOOD DELIVERY")

    def switch(self):
        self.switch_window.emit()
        self.hide()


class abc:

    def __init__(self):
        pass

    def show_first(self):
        self.firstwindow = firstwindow()
        self.firstwindow.switch_window.connect(self.show_second)
        self.firstwindow.switch_window2.connect(self.show_third)
        self.firstwindow.show()


    def show_second(self):
        self.secondwindow = secondwindow()
        self.secondwindow.switch_window.connect(self.show_first)
        self.secondwindow.show()
        self.firstwindow.hide()

    def show_third(self):
        self.thirdwindow = thirdwindow()
        self.thirdwindow.switch_window.connect(self.show_first)
        self.thirdwindow.show()
        self.firstwindow.hide()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = abc()
    controller.show_first()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()