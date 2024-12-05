import json

import requests
from sql import Sqlite
from log import logger as log

class HistoryData():
    def main(self):
        header = {"User-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 Edg/112.0.1722.48"}
        url = "http://www.17500.cn/getData/ssq.TXT"
        r = requests.get(url=url, headers=header)
        data = r.text
        lineArray = data.split("\n")
        if self.IsNoNewData(lineArray):
            # #获取数据库最后数据
            db_last_row = self.get_last_row()
            if db_last_row:
                log.info("更新双色球数据")
                self.incresa_save(lineArray,db_last_row)
            else:
                log.info("初始化双色球数据")
                self.all_save(lineArray)

    # 检查是否是最新数据？
    def IsNoNewData(self,data):
        # 获取最后一条数据
        line = data[len(data)-1]
        # 在数据库是否存在
        return self.check(line)

    # 获取最后一行书
    def get_last_row(self):
        db = Sqlite()
        return db.get_last_row()


    # 检查数据库是否存在
    def check(self,line):
        b = line.split(" ")
        db = Sqlite()
        return db.sel(b[2], b[3], b[4], b[5], b[6], b[7], b[8])

    # 按照行切割-首次全量-更新
    def all_save(self, data):
        for line in data:
            self.save(line)

    def incresa_save(self, data, last_row):
        position = data.index(last_row[9])
        for line in data[position:]:
            self.save(line)
    def save(self,line):
        db = Sqlite()
        b = line.split(" ")
        result = db.sel(b[2], b[3], b[4], b[5], b[6], b[7], b[8])
        if result:
            db.add(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], line)
            log.info(line)



