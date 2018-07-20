from django.db import models
import ast

class CompressedTextField(models.TextField):
    # from_db_value 函数用于转化数据库中的字符到 Python的变量
    def from_db_value(self, value, expression, connection, context):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def to_python(self, value):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value
    # 用于将Python变量处理后(此处为压缩）保存到数据库
    def get_prep_value(self, value):
        if not value:
            return value
        try:
            value.decode('base64')
            return value
        except Exception:
            try:
                return value.encode('utf-8').encode('bz2').encode('base64')
            except Exception:
                return value

# 保存一个 列表到数据库
class ListField(models.TextField):

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []
        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    # 用于将Python变量处理后(此处为压缩）保存到数据库
    def get_prep_value(self, value):
        if value is None:
            return value

        return list(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


# # 使用：导入ListField
# class Article(models.Model):
#     labels = ListField()




