from django.db import models
from user.models import UserProfile
from flower.models import Flower
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    flower = models.ForeignKey(Flower,on_delete=models.CASCADE,verbose_name="鲜花")
    num = models.PositiveIntegerField(default=0,verbose_name="数量")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        unique_together = ["user", "flower"]

    def __str__(self):
        return self.user.__str__() + "的购物车有" + self.flower.__str__() + str(self.num) +"个"

ORDERSTATE = (
    ("undo","未支付"),
    ("finish","已支付"),
    ("cancle","已取消")
)

class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    order_sn = models.CharField(max_length=30,null=True,blank=True,unique=True,verbose_name="订单号")
    trader_sn = models.CharField(max_length=100,unique=True,null=True,blank=True,verbose_name="交易号")
    state = models.CharField(max_length=6, choices=ORDERSTATE, verbose_name="订单状态",default="undo")
    leaveMessage = models.CharField(max_length=200, verbose_name="留言", null=True, blank=True)
    money = models.IntegerField(verbose_name="订单金额",default=90)

    reveiver = models.CharField(max_length=20,verbose_name="收货人",default="张飞")
    reveiveAddress = models.CharField(max_length=50,verbose_name="收货地址", default="郑州")
    reveivePhone = models.CharField(max_length=11,verbose_name="联系电话",default="15138001200")
    serviceTime = models.DateTimeField(verbose_name="送达时间",auto_now_add=True)
    remark = models.CharField(max_length=200,verbose_name="备注",null=True,blank=True)


    class Meta:
        verbose_name = "订单表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.__str__() + "有送给" + self.reveiver +"的订单"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="订单")
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name="鲜花")
    num = models.PositiveIntegerField(default=0, verbose_name="数量")

    class Meta:
        verbose_name = "订单详情表"
        verbose_name_plural = verbose_name
        unique_together = ["order", "flower"]

    def __str__(self):
        return self.order.__str__() + "订单有" + self.flower.__str__()
