from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20,unique=True,verbose_name="分类名")
    parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,verbose_name="父级分类",related_name="sub_cat")

    class Meta:
        verbose_name = "分类表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Flower(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="分类")
    name = models.CharField(max_length=20,verbose_name="名字")
    desc = models.CharField(max_length=100,null=True,blank=True,verbose_name="描述")
    price = models.PositiveIntegerField(verbose_name="价格")
    price_ori = models.PositiveIntegerField(verbose_name="原价")
    sales = models.PositiveIntegerField(default=0, verbose_name="销量")
    flower_language = models.CharField(max_length=200,null=True,blank=True,verbose_name="花语")
    material = models.CharField(max_length=200,null=True,blank=True,verbose_name="材质")
    distribution = models.CharField(max_length=200,default="全国")
    mainImg = models.ImageField(upload_to='flowerimg',verbose_name="主图")

    class Meta:
        verbose_name = "鲜花表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

IMGTYPE = (
    ('banner',"轮播图"),
    ('info',"图文简介")
)

class FlowerImage(models.Model):
    flower = models.ForeignKey(Flower,on_delete=models.CASCADE,verbose_name="鲜花")
    img = models.ImageField(upload_to='flowerdetailimg/',verbose_name="鲜花图文")
    type = models.CharField(max_length=6,choices=IMGTYPE,verbose_name="类型")
    index = models.IntegerField(verbose_name="顺序索引")

    class Meta:
        verbose_name = "鲜花图片"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.flower.__str__()+"的图"


