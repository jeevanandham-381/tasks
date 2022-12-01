import _mysql_connector
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="secdb"
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM details")
details=mycursor.fetchall()
for user in details:
    print(user)

