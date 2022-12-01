import mysql.connector

def fetch_all():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='thirddb',
                                             user='root',
                                             password='root')

        sql_select_Query = "select * from cse"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount,)

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
#fetch_all()
