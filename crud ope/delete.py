import mysql.connector
def delete():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="thirddb"
)

    mycursor = mydb.cursor()
    id=int(input("which id is you need to delete:"))
    val=(id,)
    sql = "delete from cse WHERE id = %s "
    #value=("vasim",3)
    mycursor.execute(sql,val)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

#delete()

