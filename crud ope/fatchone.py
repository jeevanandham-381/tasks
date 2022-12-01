import mysql.connector
def fatch_one(id):
    id = int(input("what id you want:"))

    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='thirddb',
                                         user='root',
                                         password='root')

        cursor = connection.cursor()

        sql_select_Query = """select * from cse where id=%s"""
        cursor.execute(sql_select_Query,(id,))
    # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ")
        print("\nPrinting each row")
        for row in records:
            print("Id = ", row[0],)
            print("Name = ", row[1])



    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

#fatch_one(id)
#fatch_one(3)