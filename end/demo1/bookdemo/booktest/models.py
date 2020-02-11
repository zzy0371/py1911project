from django.db import models

# Create your models here.

# MVT  M数据模型
# ORM  M数据模型
# 在此处编写应用的数据模型类
# 每一张表就是一个模型类
# 有了ORM之后我们就可以定义出表对应的模型类
# 通过操作模型类去操作数据库  不需要写sql语句

# 有了模型类之后模型类如何与数据库交互
# 1注册模型 在setting.py 中的INSTALLED_APPS 添加应用名
# 2生成迁移文件 用于与数据库交互  python manage.py makemigrations   会在对应的应用下方生成迁移文件 不需要关注
# 3执行迁移 会在对应的数据库中生成对应的表  python manage.py migrate
# 模型类更改之后需要再次生成迁移文件  执行迁移

class Book(models.Model):
    """
    book继承了Model类  应为Model类拥有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    pub_date = models.DateField(default="1983-06-01")

class Hero(models.Model):
    """
    hero继承了Model 也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=( ('male','男'),('female','女') ), default='male')
    content = models.CharField(max_length=100)
    # book  是一对多中的外键 on_delete代表删除主表数据时如何做
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
