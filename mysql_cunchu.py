import pymysql

class MysqlCunchu():
    def __init__(self):
        self.db = pymysql.connect('127.0.0.1','root','chenhe','pachong')
        self.cursor = self.db.cursor()

    def mysql_excute(self,sql,data):
        self.cursor.execute(sql,data)
        self.db.commit()

    def __del__(self):
        self.cursor.close()
        self.db.close()