
'''
 数据库（Database）这种专门用于集中存储和查询的软件.
 表是数据库中存放 关系数据 的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表等等。
 表和表之间通过外键关联。
 操作关系数据库流程：
 需要连接到数据库，一个数据库连接称为Connection。
 连接到数据库后，需要打开游标 Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
 操作完后，关闭数据库！
 1、sqlite：嵌入式数据库，适用于web和app
 2、mysql 就用它======适用于web和app
 可以直接从MySQL官方网站下载最新的Community Server 5.6.x版本:
 https://dev.mysql.com/downloads/mysql/5.6.html ！！！
 安装时，MySQL会提示输入root用户的口令，请务必记清楚。如果怕记不住，就把口令设置为password。

 MySQLdb 是用于Python链接mysql数据库的接口.
 它实现了 Python 数据库 API 规范 V2.0，基于 MySQL C API 上建立的。
 3、SQLAlchemy：687
 4、付费：Oracle，典型的高富帅，687；SQL Server，微软自家产品，Windows定制专款；

'''

'''
==========================practice 1: sqlite3: python内置数据库 ==========================
'''

# import sqlite3
#
# conn = sqlite3.connect('test_sqlite3.db')
# cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key ,name varchar(20))')
# cursor.execute('insert into user(id,name) values (\'1\',\'qsy')
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
本机安装mysql后，再安装MySQL驱动：
pip3 install mysql-connector-python --allow-external mysql-connector-python 
或者 pip3 install mysql-connector

MySQL服务器独立运行，需要支持Python的MySQL驱动来连接到MySQL服务器。
'''
# import mysql.connector
# #
# conn = mysql.connector.connect(host='localhost',
#                                port=3306,
#                                user='root',
#                                password='qsy112933',
#                                database='local_mysql'
#                                )
# # cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key ,name varchar(20))')
# # 执行插入sql语句
# cursor.execute('insert into user (id,name) values (%s,%s)',['1','我就是本地sql1'])
# cursor.execute('insert into user (id,name) values (%s,%s)',['2','我就是本地sql2'])
# cursor.execute('insert into user (id,name) values (%s,%s)',['3','我就是本地sql3'])
# # 执行删除sql语句
# cursor.execute('delete from user where id=%s and name= %s',['2','我就是本地sql2'])
# # 执行修改sql语句
# sql_update = 'update user set name=\'我就是帅\' where id=\'3\''
# try:
#     cursor.execute(sql_update)
# except:
#     conn.rollback()
# cursor.rowcount
# print('获取到游标此时对应的行数：',cursor.rowcount)
# conn.commit()
# cursor.close()
#
# cursor = conn.cursor()
# # 执行查询sql语句
# cursor.execute('select *from user where id= %s and name= %s',['1','我就是本地sql1'])
# values = cursor.fetchall()
# print('查询到游标的数据: ',values)
# cursor.close()
# conn.close()


'''
==========================practice 3: SQLAlchemy：python中最著名ORM ==========================
[
    ('1', 'Michael'),
    ('2', 'Bob'),
    ('3', 'Adam')
]
上面tuple不方便查看表的结构；

下面class实例可方便查看表的结构；
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]
这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上
python中最著名ORM:SQLAlchemy。
id需要动态调节，因为是基键！
ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。

'''

# # 导入依赖
# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# # 创建对象的基类
# Base = declarative_base()
#
# # 定义User对象
# class User(Base):
#     # 表的名字
#     __tablename__ = 'user'
#
#     # 表的结构
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#
#
# # 初始化数据库链接
# database_info = {'username':'root',
#                  'password':'qsy112933',
#                  'host':'localhost',
#                  'port':'3306',
#                  'database':'local_sqlalchemy'}
# engine = create_engine('mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'.format_map(database_info))
# # 创建DBSession类型
# DBSession = sessionmaker(bind=engine)
#
# #增加
#
# # 创建Session对象
# session = DBSession()
# # 创建User对象
# new_user = User(id='5', name='Bob')
# session.add(new_user)
# # 提交
# session.commit()
# # 关闭session
# session.close()
#
#
# # 查询
# # 创建session
# session = DBSession()
# # 利用session创建查询，query(对象类).filter(条件).one()/all()
# user = session.query(User).filter(User.id=='5').one()
# print('type:{0}'.format(type(user)))
# print('name:{0}'.format(user.name))
# # 关闭session
# session.close()
#
#
# # 更新
# session = DBSession()
# user_result = session.query(User).filter_by(id='1').first()
# user_result.name = "jack"
# session.commit()
# session.close()
#
#
# # 删除
# session = DBSession()
# user_willdel = session.query(User).filter_by(id='1').first()
# session.delete(user_willdel)
# session.commit()
# session.close()

'''
==========================practice 4: PyMySQL：py可用的mysql ==========================
pip3 install Pymysql
'''

import pymysql

db = pymysql.connect('localhost','root','qsy112933','local_python_mysql')
cusor = db.cursor()

cusor.execute('SELECT VERSION()')
data = cusor.fetchall()
print('Database version :%s'%data)
cusor.close()
db.close()


db = pymysql.connect('localhost','root','qsy112933','local_python_mysql',charset='utf8')
cusor = db.cursor()

# 如果有就删除
sql_del = 'drop table if exists employee'
cusor.execute(sql_del)
sql_create = 'create table employee (id varchar(20) primary key,sex varchar(20))'
cusor.execute(sql_create)
cusor.execute('insert into employee(id,sex) values (%s,%s)',['1','男'])
db.commit()
db.close()
