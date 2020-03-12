from django.shortcuts import render
from rest_framework import viewsets,mixins,permissions
from .models import *
from .serializer import *
# Create your views here.

class CommentViewSets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin):
    """
    list 评论列表
    create 创建评论
    delete 删除评论
    """
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return CommentDetailSerializer
        else:
            return CommentSerializer
#     TODO 添加评论时添加评论图



class UserFavViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin):
    """
    list 收藏列表
    create 添加收藏
    destroy 删除收藏
    """
    queryset = Collect.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        print(self.request.user)
        return Collect.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        else:
            return UserFavSerializer
