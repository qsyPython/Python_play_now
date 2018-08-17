'''
Models for user,blog,comment
'''
import time,uuid
from orm import Model,StringField,BooleanField,FloatField,IntegerField,TextField

def next_id():
    return '%015d%s000' % (int(time.time()*1000),uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key = True,default=next_id,ddl ='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)
https://github.com/michaelliao/awesome-python3-webapp/blob/day-04/www/models.py
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014323389656575142d0bcfeec434e9639a80d3684a7da000
