
'''
 数据库（Database）这种专门用于集中存储和查询的软件.
 表是数据库中存放 关系数据 的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表等等。
 表和表之间通过外键关联。
 操作关系数据库流程：
 需要连接到数据库，一个数据库连接称为Connection。
 连接到数据库后，需要打开游标Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
 操作完后，关闭数据库！
 1、sqlite：嵌入式数据库，适用于web和app
 2、mysql 就用它======适用于web和app
 可以直接从MySQL官方网站下载最新的Community Server 5.6.x版本:
 https://dev.mysql.com/downloads/mysql/5.6.html ！！！
 安装时，MySQL会提示输入root用户的口令，请务必记清楚。如果怕记不住，就把口令设置为password。

 MySQLdb 是用于Python链接mysql数据库的接口.
 它实现了 Python 数据库 API 规范 V2.0，基于 MySQL C API 上建立的。
 3、SQLAlchemy：
 4、付费：Oracle，典型的高富帅，687；SQL Server，微软自家产品，Windows定制专款；

'''

'''
==========================practice 1: sqlite: python内置 ==========================
'''

# import sqlite3
#
# conn = sqlite3.connect('test_sqlite.db')
# cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key ,name varchar(20))')
# cursor.execute('insert into user(id,name) values (\'1\',\'qsy\')')
# print('获取插入的行数: ',cursor.rowcount)
# cursor.execute('select *from user where id=? and name=?',('1','qsy'))
# values = cursor.fetchall()
# print('获取到查询的语句：',values)
# cursor.close()
#
# conn.commit()
# conn.close()


'''
==========================practice 2: mysql ==========================
MySQL服务器独立运行，需要支持Python的MySQL驱动来连接到MySQL服务器
'''
import mysql.connector

conn = mysql.connector.connect(host='localhost',
                               port = 3306,
                               user = 'root',
                               password='qsy112933',
                               database='test11'
                               )
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key ,name varchar(20))')
cursor.execute('insert into user (id,name) values (%s,%s)',['1','我就测测而已'])
cursor.rowcount
print('获取到对应的行数：',cursor.rowcount)
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select *from user where id= %s',('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

'''
==========================practice 3: PyMySQL ==========================
'''
# import pymysql
#
# db = pymysql.connect('localhost','qsy123','qsy123','test_sqlite')
# cusor = db.cursor()
#
# cusor.execute('SELECT VERSION()')
# data = cusor.fetchall()
# print('Database version :%s'%data)
#
# db.close()