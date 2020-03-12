"""hualiservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#媒体资源路由
from django.conf.urls import url,include
from django.views.static import serve
from .settings import MEDIA_ROOT

# API文档
from rest_framework.documentation import include_docs_urls

# 引入用户应用视图
from user.views import UserViewSets,ReceiveAddressViewSets
from flower.views import FlowerViewSets,CategoryViewSets
from user_operate.views import UserFavViewset,CommentViewSets
from trade.views import CartViewSets,OrderViewSets
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh,token_verify


# 注册路由
from rest_framework import routers
router = routers.DefaultRouter()
router.register('users',UserViewSets)
router.register('receiveaddress',ReceiveAddressViewSets)

router.register('categorys',CategoryViewSets)
router.register('flowers',FlowerViewSets)

router.register(r'userfavs', UserFavViewset)
router.register(r'comments', CommentViewSets)

router.register(r'carts', CartViewSets)
router.register(r'orders', OrderViewSets)




urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url('api/v1/docs/',include_docs_urls(title="花礼网接口文档")),

    url('api/v1/users/login/',token_obtain_pair),
    url('api/v1/users/refresh/',token_refresh),
    url('api/v1/users/verify/',token_verify),


    path('api/v1/',include(router.urls)),
    path('',include('rest_framework.urls')),
]
