import mysql.connector
def add_user():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="thirddb"
  )

  mycursor = mydb.cursor()

  #sql =" insert into cse(id, name) VALUES (1,'jeeva')"
  #sql =" insert into cse(id, name) VALUES (2,'kalai')"
  r=int(input("enter id:\n"))
  n=input("enter your name:\n")

  s='insert into cse values (%s,%s)'
  #val =(1, "jeeva")
  t=(r,n)
  mycursor.execute(s,t)
  print("user added")

  mydb.commit()
#add_user()

  #print(mycursor.rowcount, "record inserted.")



