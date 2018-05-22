import sqlite3

class mySQLManager(object):
    def __init__(self):
        self.creat_table()

    def connect_mysql(self):
        cnx = sqlite3.connect("agen_db.db")
        return cnx

#创建表
    def creat_table(self):

        db = self.connect_mysql()
        cus = db.cursor()
        ips = '''create table if not exists IPs(
                   ip varchar(100) not null,port int not null,protocolType varchar(5) not null
           ) '''
        cus.execute(ips)
        # # 关闭数据库连接
        db.close()
#插入ip、port、protocolType
    def insert_ip_table(self,ipDic):
        if len(ipDic) > 0:
            db = self.connect_mysql()
            cus = db.cursor()
            # SQL 插入语句
            sql = "insert into IPs('ip','port','protocolType') \
                          values ('%s','%d','%s')" %(ipDic['ip'],ipDic['port'],ipDic['type'])
            try:
                # 执行sql语句
                result = cus.execute(sql)
                print(result)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                db.rollback()

            # 关闭数据库连接
            db.close()
#返回所有数据
    def select_all(self):
        db = self.connect_mysql()
        cus = db.cursor()
        # SQL 查询语句
        sql = "select * from IPs"
        try:
            # 执行SQL语句
            cus.execute(sql)
            # 获取所有记录列表
            results = cus.fetchall()
            ips = []
            for row in results:
                ips.append({'ip':row[0],'port':row[1],'type':row[2]})
            db.close()
            return ips
        except:
            return None

#查询ip
    def select_ip(self,ip):
        db = self.connect_mysql()
        cus = db.cursor()
        # SQL 查询语句
        sql = "select 1 from IPs \
               where ip = '%s' limit 1" % (ip)
        isExit = False
        try:
            # 执行SQL语句
            cus.execute(sql)
            # 获取所有记录列表
            results = cus.fetchall()
            if len(results)> 0:
                isExit = True
        except:
            pass

        # 关闭数据库连接
        db.close()
        return isExit
#删除ip
    def delete_ip(self,ip):
        db = self.connect_mysql()
        cus = db.cursor()
        # SQL 删除语句
        sql = "delete from IPs where ip = '%s'" % (ip)
        try:
            # 执行SQL语句
            cus.execute(sql)
            # 提交修改
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭连接
        db.close()