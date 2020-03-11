from django.shortcuts import render
from rest_framework import viewsets,mixins
from .models import *
from .serializer import *
from rest_framework import permissions
# Create your views here.

class CategoryViewSets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FlowerViewSets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer


