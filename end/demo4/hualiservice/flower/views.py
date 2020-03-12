from django.shortcuts import render
from rest_framework import viewsets,mixins
from .models import *
from .serializer import *
from rest_framework import permissions
# Create your views here.

class CategoryViewSets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    """
    list：展示分类列表
    retrieve：展示单个分类详情
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FlowerViewSets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    """
    list：展示所有鲜花
    retrieve：展示鲜花详情
    """
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer


