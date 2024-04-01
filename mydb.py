import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',

)
cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE student_info")

print("All Done!")
