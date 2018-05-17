import sqlite3
from  AQModel import AQModel
class SQliteAQIModel(object):
    def __init__(self):
        self.db = None

    def sqlConnect(self):
        try:
            self.db = sqlite3.connect('SQliteAQI.db')
            sql_createTable =  """CREATE TABLE IF NOT EXISTS `AQITable` (
                                    `name` CHAR(512) NOT NULL,
                                    `aqvalue` TEXT NOT NULL)"""

            self.db.execute(sql_createTable)
        except Exception as e:
            print("数据库连接失败." + str(e))



    def close(self):
        try:
            if self.db is not None:
                self.db.close()
        except BaseException as e:
            print('数据库关闭失败', + str(e))


    def insert_table_dict(self,aqModel = AQModel):
        if aqModel is None:
            return False
        try:
            cols = aqModel.name
            value = aqModel.aqiValue
            flag = self.selectAQI(aqModel)
            if flag == True:
                self.db.execute('update  AQITable set aqvalue =? WHERE name =?',(value,cols,))
            else:
                 sql_insert = "insert into AQITable (name,aqvalue) VALUES (:name_value,:aqi_value)"
                 self.db.execute(sql_insert,{'name_value':cols,'aqi_value':value})
            self.db.commit()
            return True
        except BaseException as e:
            self.db.rollback()
            return False
            print("sqlite3 insert error." + str(e))


    def deleteAQI(self,aqModel = AQModel):
        try:
            cols = aqModel.name
            self.db.execute('delete from AQITable where name=?', (cols,))
            self.db.commit
            return True
        except BaseException as e:
            self.db.rollback()
            return False
            print("sqlite3 insert error." + str(e))


    def deleteAllAQI(self):
        try:
            # sql = 'delete from AQITable'
            # self.db.execute(sql)
            # self.db.commit
            self.db.execute('drop table AQITable')
            self.db.commit
            return True
        except BaseException as e:
            self.db.rollback()
            return False
            print("sqlite3 insert error." + str(e))


    def selectAQI(self,aqModel = AQModel):
        try:
            cols = aqModel.name
            cursor = self.db.cursor()
            cursor.execute('select * from AQITable where name=?', (cols,))
            values = cursor.fetchone()
            if values != None:
                return True
            else:
                return False
        except BaseException as e:
            self.db.rollback()
            return False
            print("sqlite3 insert error." + str(e))


    def getAllAQI(self):
        sql_Select = "select * from AQITable"
        cursor = self.db.cursor()
        cursor.execute(sql_Select)
        list = []
        for tt in cursor.fetchall():
            aqi = AQModel(tt[0],int(tt[1]))
            list.append(aqi)
        return self.operatorSort(list)

    def operatorSort(self,persons = []):
        try:
            import operator
        except ImportError:
            cmpfun = lambda x: x.aqiValue
        else:
            cmpfun = operator.attrgetter("aqiValue", "name")

        persons.sort(key=cmpfun, reverse=True)
        xlist = []
        ylist = []
        for aq in persons:
            xlist.append(aq.name)
            ylist.append(aq.aqiValue)
        return (xlist,ylist)