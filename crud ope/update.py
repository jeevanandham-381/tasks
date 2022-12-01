import mysql.connector

def update():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="thirddb"
    )

    mycursor = mydb.cursor()
    id=int(input("which id is you need to update:"))
    name=input("the replace name:")
    val=(name,id)
    sql = "UPDATE cse SET name = %s WHERE id = %s"
    #value=("vasim",3)
    mycursor.execute(sql,val)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")
#update()
