from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your views here.
SEX = (
    ("male","男"),
    ("female","女"),
    ("secret","保密")
)

class UserProfile(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="邮箱")
    username = models.CharField(max_length=10,unique=True,null=True,blank=True,verbose_name="用户名")
    telephone = models.CharField(max_length=11,null=True,blank=True,verbose_name="手机号")
    # headImg 需要安装Pillow模块
    headImg = models.ImageField(upload_to="head/",default="head/default_head.png", verbose_name="头像")
    sex = models.CharField(max_length=6,choices=SEX,default="secret", verbose_name="性别")
    birthday = models.DateField(null=True,blank=True,verbose_name="生日")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username or self.email


class ReceiveAddress(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    name = models.CharField(max_length=10,verbose_name="收货人")
    telephone = models.CharField(max_length=11,verbose_name="手机号")
    address = models.CharField(max_length=50,verbose_name="地址")
    addressDetail = models.CharField(max_length=50,verbose_name="详细地址")
    isDefault = models.BooleanField(default=False,verbose_name="默认地址")

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.__str__()+"的收货地址"
