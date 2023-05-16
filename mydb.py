import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

#preparar un objeto cursor
cursorObject = dataBase.cursor()

#crear una database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
