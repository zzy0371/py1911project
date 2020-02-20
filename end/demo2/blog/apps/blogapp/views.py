from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'index.html')
    # return HttpResponse("首页")
    # return re

def detail(request,articleid):
    return render(request,'single.html')
    # return HttpResponse("文章"+articleid)

def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("联系我们")