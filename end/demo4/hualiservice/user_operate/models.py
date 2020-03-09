from django.db import models
from user.models import UserProfile
from flower.models import Flower
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    flower = models.ForeignKey(Flower,on_delete=models.CASCADE,verbose_name="鲜花")
    rate = models.PositiveIntegerField(default=0,verbose_name="评星")
    comment = models.CharField(max_length=200,verbose_name="评论")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="评论时间")

    class Meta:
        verbose_name = "评论表"
        verbose_name_plural = verbose_name
        unique_together = ["user","flower"]

    def __str__(self):
        return self.user.__str__()+"评论"+self.flower.__str__()

class CommentImg(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,verbose_name="评论")
    img = models.ImageField(upload_to="commentimg/",verbose_name="评论图")

    class Meta:
        verbose_name = "评论图表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment.__str__()+"的评论图"


class Collect(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    flower = models.ForeignKey(Flower,on_delete=models.CASCADE,verbose_name="鲜花")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="收藏时间")

    class Meta:
        verbose_name = "收藏表"
        verbose_name_plural = verbose_name
        unique_together = ["user", "flower"]

    def __str__(self):
        return self.user.__str__()+"收藏"+self.flower.__str__()