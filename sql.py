import datetime
import sqlite3

class Sqlite:
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    def __init__(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS history
               (ID CHAR(20) PRIMARY KEY  NOT NULL,
               DateTime CHAR(20) NOT NULL,
               Red1 INT NOT NULL,
               Red2 INT NOT NULL,
               Red3 INT NOT NULL,
               Red4 INT NOT NULL,
               Red5 INT NOT NULL,
               Red6 INT NOT NULL,
               Blue INT NOT NULL,
               Desc CHAR(100));''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS generation
               (ID INTEGER PRIMARY KEY ,
               DateTime CHAR(20)    NOT NULL,
               Red1 INT NOT NULL,
               Red2 INT NOT NULL,
               Red3 INT NOT NULL,
               Red4 INT NOT NULL,
               Red5 INT NOT NULL,
               Red6 INT NOT NULL,
               Blue INT NOT NULL,
               desc CHAR(100));''')
        self.conn.commit()
    def sel(self,r1,r2,r3,r4,r5,r6, b1):
        sql = ("SELECT * from history where "
               " Red1 ={} and Red2 ={} and Red3 ={} and Red4 ={} and Red5 ={} and Red6 ={} and "
               " Blue ={} ").format(r1,r2,r3,r4,r5,r6,b1)    # 不设置指定位置，按默认顺序
        result = self.c.execute(sql)
        one = result.fetchone()
        return True if one is None else False

    def get_last_row(self):
        query = f"SELECT * FROM history ORDER BY id DESC LIMIT 1;"
        result = self.c.execute(query)
        return result.fetchone()



    def add(self,id,date,r1,r2,r3,r4,r5,r6, b1,desc):
        sql = ("INSERT INTO history (ID,DateTime,Red1,Red2,Red3,Red4,Red5,Red6,Blue,Desc)"
               "VALUES ({},'{}',{},{},{},{},{},{},{},'{}')".format(id,date,r1,r2,r3,r4,r5,r6, b1,desc))
        self.c.execute(sql)
        self.conn.commit()

    def addNew(self,r1, r2, r3, r4, r5, r6, b1):
        now = datetime.datetime.now()
        sql = ("INSERT INTO generation (DateTime,Red1,Red2,Red3,Red4,Red5,Red6,Blue)"
               "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(now,r1,r2,r3,r4,r5,r6, b1))
        self.c.execute(sql)
        self.conn.commit()

    def gsel(self,r1,r2,r3,r4,r5,r6, b1):
        sql = ("SELECT * from generation where "
               " Red1 ={} and Red2 ={} and Red3 ={} and Red4 ={} and Red5 ={} and Red6 ={} and "
               " Blue ={} ").format(r1,r2,r3,r4,r5,r6,b1)    # 不设置指定位置，按默认顺序

        result = self.c.execute(sql)
        one = result.fetchone()
        return True if one is None else False

