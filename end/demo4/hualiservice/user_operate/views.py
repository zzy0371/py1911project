from django.shortcuts import render
from rest_framework import viewsets,mixins,permissions
from .models import *
from .serializer import *
# Create your views here.

class CommentViewSets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return CommentDetailSerializer
        else:
            return CommentSerializer

class UserFavViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
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
