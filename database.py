import mysql.connector

mydb = mysql.connector.connect(
    host="Localhost",
    user="root",
    passwd="asdfghjkl",
    database="login"
)
mycursor= mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS id(uname VARCHAR(40),passwd VARCHAR(32))")
mydb.commit()


#def newsign1(self):
#    self.window = QtWidgets.QMainWindow()
 #   self.ui = Ui_MainWindow1()
  #  self.ui.setup(self.window)
   # self.window.show()


#def indb(self):
  #  uname = self.l2.text()
   # passwd = self.l4.text()
   # sqlquery = "INSERT INTO id VALUES(%s,%s)"
   # user = (uname, passwd)
   # mycursor.execute(sqlquery, user)
   # mydb.commit()
  #  MainWindow2.destroy()


self.le1.setMaxLength(32)
        self.le3.setMaxLength(10)
        self.le4.setMaxLength(40)
        self.le5.setMaxLength(32)
        self.lb5.setEchoMode(QtWidgets.QLineEdit.Password)

