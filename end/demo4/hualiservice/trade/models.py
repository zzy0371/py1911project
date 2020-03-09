from django.db import models
from user.models import UserProfile
from flower.models import Flower
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    flower = models.ForeignKey(Flower,on_delete=models.CASCADE,verbose_name="鲜花")
    num = models.PositiveIntegerField(default=0,verbose_name="数量")
    price = models.PositiveIntegerField(verbose_name="价格")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        unique_together = ["user", "flower"]

    def __str__(self):
        return self.user.__str__() + "的购物车有" + self.flower.__str__() + str(self.num) +"个"

ORDERSTATE = (
    ("undo","未支付"),
    ("finish","已支付")
)

class Order(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    reveiver = models.CharField(max_length=20,verbose_name="收货人")
    serviceTime = models.DateTimeField(verbose_name="送达时间")
    leaveMessage = models.CharField(max_length=200,verbose_name="留言",null=True,blank=True)
    remark = models.CharField(max_length=200,verbose_name="备注",null=True,blank=True)
    state = models.CharField(max_length=6,choices=ORDERSTATE,verbose_name="状态")

    class Meta:
        verbose_name = "订单表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.__str__() + "有送给" + self.reveiver +"的订单"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="订单")
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name="鲜花")
    num = models.PositiveIntegerField(default=0, verbose_name="数量")
    price = models.PositiveIntegerField(verbose_name="价格")

    class Meta:
        verbose_name = "订单详情表"
        verbose_name_plural = verbose_name
        unique_together = ["order", "flower"]

    def __str__(self):
        return self.order.__str__() + "订单有" + self.flower.__str__()
