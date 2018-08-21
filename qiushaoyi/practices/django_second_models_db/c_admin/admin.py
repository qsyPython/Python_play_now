from django.contrib import admin
from .models import Article,Person

# 控制admin后台显示哪些fields，默认是title
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time','content',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAdmin)
