from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name="分类名")
    def __str__(self):
        return self.name

class Good(models.Model):
    name = models.CharField(max_length=20,verbose_name="商品名字")
    desc = models.CharField(max_length=100,null=True,blank=True,verbose_name="商品描述")
    # 在序列化关联模型时一定要声明related_name
    # 一找多 related_name 没有定义  c1.good_set.all()   related_name定义了  c1.goods.all()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="分类",related_name='goods')

    def __str__(self):
        return self.name
