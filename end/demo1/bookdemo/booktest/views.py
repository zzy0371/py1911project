from django.shortcuts import render
from django.template import loader
from .models import Book,Hero
# Create your views here.

# MVT  中的V视图模块
# 在此处接受请求 处理数据 返回响应

# 3编写对应的视图函数
from django.http import HttpResponse
def index(request):
    # return HttpResponse("这里是 <h1>首页</h1> ")

    # 1获取模板
    # template = loader.get_template('index.html')
    # 2渲染模板数据
    books = Book.objects.all()
    # context = {"books": books}
    # result = template.render(context)
    # 3将渲染结果使用httpresponse返回
    # return HttpResponse(result)

    # 3合1
    return render(request,'index.html',{"books":books})

def detail(request,bookid):
    # return HttpResponse("这里是详情页"+bookid)
    # template = loader.get_template('detail.html')
    book  = Book.objects.get(id=bookid)
    # context = {"book":book}
    # result = template.render(context)
    # return HttpResponse(result)

    return render(request,'detail.html',{"book":book})


def about(request):
    return HttpResponse("这里是关于")

# 使用django 模板
# MVT
