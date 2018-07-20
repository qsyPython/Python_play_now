
#========= # QuerySet基础使用 =========
# from django.db import models

# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
#
# class Entry(models.Model):
#
#     # 在django2.0后，定义外键ForeignKey 和一对一 OneToOneField关系的时候需要加on_delete选项
#     b_blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#
#     # 额外建表：blog_entry_authors
#     authors = models.ManyToManyField(Author)
#     n_comments = models.IntegerField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     def __str__(self):
#         return self.headline


#========= # QuerySet进阶使用 # =========

# from __future__ import unicode_literals
# from django.db import models
# from django.utils.encoding import python_2_unicode_compatible
# from django.contrib import admin
#
# @python_2_unicode_compatible
# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     qq = models.CharField(max_length=10)
#     addr = models.TextField()
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
# @python_2_unicode_compatible
# class Article(models.Model):
#     title = models.CharField(max_length=50)
#     author = models.ForeignKey(Author,on_delete=models.CASCADE)
#     content = models.TextField()
#     score = models.IntegerField()
#     tags = models.ManyToManyField('Tag') #会单门建table
#
#     def __str__(self):
#         return self.title
#
# @python_2_unicode_compatible
# class Tag(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name

# =========# Django 自定义Field #=========

# from django.db import models
#
# class CompressedTextField(models.Model):
#     def from_db_value(self, value, expression, connection, context):
#         if not value:
#             return value
#         try:
#             return value.decode('base64').decode('bz2').decode('utf-8')
#         except Exception:
#             return value
#
#     def to_python(self,value):
#         if not value:
#             return value
#         try:
#             value.decode('base64')
#             return value
#         except Exception:
#             try:
#                 return value.encode('utf-8').encode('bz2').encode('base64')
#             except Exception:
#                 return value


# =========# Django 后台 #=========
from  django.db import models
class Article(models.Model):
    title = models.CharField(u'标题',max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间',auto_now_add=True,editable=True)
    update_time = models.DateField(u'更新时间',auto_now=True,null=True)

    def __str__(self):
        return self.title;




