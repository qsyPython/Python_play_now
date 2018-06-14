# Windows7下Python3.x使用MySQL数据库(安装教程)
# https://blog.csdn.net/c406495762/article/details/56279888?locationNum=5&fps=1
# 配置好之后要手动创建一个数据库，否则会出现找不到的错误
# https://www.cnblogs.com/jiangxiaobo/p/7089345.html

import pymysql

class MySQLCreate(object):

    @staticmethod
    def sql_connect():
        # 创建连接，指定数据库的ip地址，账号、密码、端口号、要操作的数据库、字符集
        return pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', database='test',charset='utf8')
        # 创建游标
        self.cursor = self.db.cursor()


    def create_form(self):
        db = MySQLCreate.sql_connect()
        db.cursor().execute('create table region_info (province varchar(500), city varchar(3000))')
        db.cursor().execute('create table city_info (city_name varchar(500), city_url varchar(3000))')

    def rangion_insert_data(self, province_key, city_value):
        try:
            db = MySQLCreate.sql_connect()
            cursor = db.cursor()
            sql_str = "INSERT INTO region_info(province,city)" \
                      "VALUES ('%s', '%s' )" % (province_key, city_value)
            cursor.execute(sql_str)
            db.commit()
        except:
            db.rollback()
            raise
        finally:
            cursor.close()
            db.close()


    def city_insert_data(self, city_key, html_value):
        try:
            db = MySQLCreate.sql_connect()
            cursor = db.cursor()
            sql_str = "INSERT INTO city_info(city_name,city_url)" \
                      "VALUES ('%s', '%s' )" % (city_key, html_value)
            cursor.execute(sql_str)
            db.commit()
        except:
            db.rollback()
            raise
        finally:
            cursor.close()
            db.close()


    def rangion_search_all_data(self):
        try:
            db = MySQLCreate.sql_connect()
            cursor = db.cursor()
            sql_str = "select * from region_info"
            cursor.execute(sql_str)
            value = cursor.fetchall()
            return value
        except:
            db.rollback()
        finally:
            cursor.close()
            db.close()


    def rangion_search_city(self,p):
        try:
            db = MySQLCreate.sql_connect()
            cursor = db.cursor()
            sql_str = "select * from region_info where province = '%s'" % (p)
            cursor.execute(sql_str)
            value = cursor.fetchall()
            return value[0][1]
        except:
            db.rollback()
        finally:
            cursor.close()
            db.close()

    def search_html(self,c):
        try:
            db = MySQLCreate.sql_connect()
            cursor = db.cursor()
            sql_str = "select * from city_info where city_name = '%s'" % (c)
            cursor.execute(sql_str)
            value = cursor.fetchall()
            return value[0][1]
        except:
            db.rollback()
        finally:
            cursor.close()
            db.close()