from django.db import models

# 创建了worker的表
class Worker(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self):
        return self.name + str(self.age)


# 创建了student的表
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name






