from django.contrib import admin
# 定义后端显示界面
from django.contrib.admin import ModelAdmin
# Register your models here.
# django自带的后台管理操作需要再此处实现
# 注册自己需要管理的模型 Book Hero
from .models import Book,Hero,User
class HeroInline(admin.StackedInline):
    """
    定义关联类
    """
    model = Hero
    extra = 1

class HeroAdmin(ModelAdmin):
    list_display = ('name','gender','content','book')
    search_fields = ('gender',)

admin.site.register(Hero,HeroAdmin)

class BookAdmin(ModelAdmin):
    """
    定义模型管理类
    通过该类可以修改后台页面
    """
    # 更改后端显示列
    list_display = ('title','price','pub_date')
    # 每页显示1个
    # list_per_page = 1
    # 定义后端搜索字段
    search_fields = ('title','price')
    # 指定过滤字段
    list_filter = ('title','price')
    inlines = [HeroInline]

admin.site.register(Book,BookAdmin)


admin.site.register(User)





