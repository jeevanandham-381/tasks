from connections import mysql
class getData(object):
    def __init__(self):
        self.cursor=mysql.connect().cursor()
    def gatalldata(self):
        self.cursor.execte("SELECT * FROM CSE")
        aData=self.cursor.fetchall()
        return aData