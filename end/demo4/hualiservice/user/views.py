from django.shortcuts import render

from rest_framework import viewsets, generics, mixins, status,permissions
from rest_framework.response import Response
from rest_framework.decorators import action,api_view,permission_classes
from .models import *
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken



class ReceiveAddressViewSets(viewsets.ModelViewSet):
    queryset = ReceiveAddress.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return ReceiveAddress.objects.filter(user=self.request.user)
    serializer_class = ReceiveAddressSerializer

class UserViewSets(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin):
    queryset = UserProfile.objects.all()

    @action(methods=["POST"],detail=False)
    def forget(self,request):
        print("当前用户",request.user,request.data)
        user = UserProfile.objects.filter(telephone=request.data["telephone"]).first()
        if user:
            seria = UserResetPasswordSerializer(instance=user, data=request.data)
            seria.is_valid(raise_exception=True)
            seria.save()
            return Response("密码修改成功")
        else:
            return Response("当前手机号未注册")

    @action(methods=["POST"],detail=False)
    def sendmsg(self,request):
        seria = UserCodeSerializer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response("发送验证码成功")

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegistSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == "retrieve" or self.action=="update":
            return [permissions.IsAuthenticated()]
        return []

    def perform_create(self, serializer):
        return serializer.save()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        re_dict = serializer.data
        re_dict["id"] = user.id
        re_dict["token"] = str(RefreshToken.for_user(user).access_token)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)