import mysql.connector

mydb = mysql.connector.connect(
    host="Localhost",
    user="root",
    passwd="asdfghjkl",
    database="login")
mycursor= mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS id(uname VARCHAR(40),passwd VARCHAR(32))")
mydb.commit()

uname = "123"
passwd = "123"
sqlquery = "INSERT INTO id VALUES(%s,%s)"
user = (uname, passwd)
mycursor.execute(sqlquery, user)
mydb.commit()

if (mycursor.execute("SELECT * FROM 'id' WHERE 'uname'='" + uname + "' AND 'passwd'='" + passwd + "'")):
    mydb.commit()
    print("done")