# 引入路由绑定函数
from django.conf.urls import url
from . import views


app_name = "booktest"

# 2,每一个路由文件中必须编写路由数组
urlpatterns = [
    # 应用中真正的地址为  /booktest/index/

    # url 第一个参数为正则表达式 为了匹配输入的网址  第二个参数为需要执行的视图函数
    # url(r'^index/$',views.index),
    url(r'^$',views.index,name='index'),

    # 使用正则分组可以向视图函数中传递参数
    # 第一个参数就是路由 第二个参数就是视图函数
    # 第一个参数中如果有正则分组  小括号  则正则分组匹配的内容会作为实参传递给视图函数
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^about/$',views.about,name='about'),

    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),

    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^edithero/(\d+)/$',views.edithero,name='edithero'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),

]