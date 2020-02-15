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
    title = models.CharField(max_length=20,verbose_name="图书名")
    price = models.FloatField(default=0)
    pub_date = models.DateField(default="1983-06-01")
    author = models.CharField(max_length=20,default="zzy")
    desc = models.CharField(max_length=50,null=True,blank=True,db_column='description',help_text='请输入书籍备注嘻嘻')
    # telephone = models.CharField(max_length=11, unique=True)

    def __str__(self):
        # 此处必须返回字符串
        return self.title

class Hero(models.Model):
    """
    hero继承了Model 也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=( ('male','男'),('female','女') ), default='male')
    content = models.CharField(max_length=100)
    # book  是一对多中的外键 on_delete代表删除主表数据时如何做
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# django orm关联查询
# 多方Hero   一方Book
# 1多找一， 多方对象.关系字段    exp: h1.book
# 2一找多， 一方对象.小写多方类名_set.all()   exp:  b1.hero_set.all()


class UserManager(models.Manager):
    """
    自定义模型管理类  该模型不在具有objects对象
    """
    def deleteByTelePhone(self,tele):
        # django默认的objects 是Manager类型    *.objects.get()
        user = self.get(telephone=tele)
        user.delete()
    def createUser(self,tele):
        # self.model可以获取模型类构造函数
        user = self.model()
        # user = User()
        user.telephone = tele
        user.save()

class User(models.Model):
    telephone = models.CharField(max_length=11,null=True,blank=True,verbose_name="手机号码")
    # 自定义过管理字段之后不在有objects  自定义了一个新的objects
    objects = UserManager()
    def __str__(self):
        return self.telephone
    class Meta:
        # 表明
        db_table = "用户类"
        ordering = ["-telephone"]
        # admin页面进入模型类显示名字
        verbose_name = "用户模型类a"
        # admin 页面在应用下方显示的模型名
        verbose_name_plural = "用户模型类s"
