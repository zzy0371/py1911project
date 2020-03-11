from django.shortcuts import render
from rest_framework import viewsets,mixins,permissions
from .models import *
from .serializer import *
# Create your views here.

class CartViewSets(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cart.objects.all()
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return CartDetailSerializer
        else:
            return CartSerializer