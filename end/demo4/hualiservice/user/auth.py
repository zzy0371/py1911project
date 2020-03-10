from django.contrib.auth.backends import BaseBackend
from .models import UserProfile
from django.db.models import Q
class MyLoginBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        username = kwargs["username"]
        user = UserProfile.objects.filter(Q(email=username) | Q(telephone=username) | Q(username=username) ).first()
        if user:
           if user.check_password(kwargs["password"]):
               return user
        return None
