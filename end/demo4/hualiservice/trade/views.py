from django.shortcuts import render
from rest_framework import viewsets,mixins,permissions
from .models import *
from .serializer import *
# Create your views here.

class CartViewSets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    """
    list 查看购物车所有商品
    create 添加商品
    delete 删除商品
    patch 修改商品数量
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cart.objects.all()
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return CartDetailSerializer
        else:
            return CartSerializer

class OrderViewSets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.CreateModelMixin):
    """
    list 查看所有订单
    create 创建订单
    delete 取消订单
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return OrderDetailSerializer
        else:
            return OrderSerializer
    def perform_create(self, serializer):
        """
        创建订单时将购物车中商品加入订单
        """
        order = serializer.save()
        order.money=0
        flowers = Cart.objects.filter(user=self.request.user)
        for f in flowers:
            orderDetail = OrderDetail()
            orderDetail.flower=f.flower
            orderDetail.num = f.num
            orderDetail.order = order
            orderDetail.save()
            order.money += orderDetail.flower.price * orderDetail.num
            order.save()
            f.delete()
        return order
