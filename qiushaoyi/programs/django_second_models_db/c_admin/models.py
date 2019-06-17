from __future__ import unicode_literals
from django.db import models

# 兼容python2.x和python3.x
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(u'我是标题',max_length=256)
    content = models.TextField(u'我是内容你知道么')
    pub_date = models.DateTimeField(u'发表时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)
    def __str__(self):# 重写，刷新后台网页，可返回对应的title
        return self.title


@python_2_unicode_compatible
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "full name of the person"
    full_name = property(my_property)