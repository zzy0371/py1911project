from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    ads = Ads.objects.all()

    # locals可以返回作用域局部变量
    # print(locals())

    return render(request,'index.html',locals())
    # return HttpResponse("首页")
    # return re


def detail(request,articleid):
    return render(request,'single.html')
    # return HttpResponse("文章"+articleid)

def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("联系我们")

def favicon(request):
    # 如果获取logo则重定向到一个图片资源
    return redirect(to="/static/favicon.ico")