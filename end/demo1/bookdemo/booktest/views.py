from django.shortcuts import render,redirect,reverse
from django.template import loader
from .models import Book,Hero
# Create your views here.

# MVT  中的V视图模块
# 在此处接受请求 处理数据 返回响应

# 3编写对应的视图函数
from django.http import HttpResponse,HttpResponseRedirect
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
    smallbook = Book.objects.filter(id__gt=100)
    # 3合1
    return render(request,'index.html',{"books":books,"smallbook":smallbook,"name1":"zzy<h3>三级标题</h3>"})

def detail(request,bookid):
    # return HttpResponse("这里是详情页"+bookid)
    # template = loader.get_template('detail.html')
    book  = Book.objects.get(id=bookid)
    # context = {"book":book}
    # result = template.render(context)
    # return HttpResponse(result)

    return render(request,'detail.html',{"book":book})

def deletebook(request,bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # return HttpResponse("删除成功")
    # 删除一本书之后仍然回到列表页
    # return HttpResponseRedirect(redirect_to='/')

    # 在view视图中解除硬编码
    url = reverse("booktest:index")
    # return redirect(to="/")
    return redirect(to=url)

def addhero(request,bookid):
    # 视图函数中可以同时纯在get与post请求  默认为get
    if request.method == "GET":
        return render(request,'addhero.html')
    elif request.method == "POST":
        hero = Hero()
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:detail",args=(bookid,))
        return  redirect(to=url)


def edithero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    # 使用get方法进入英雄的编辑页面
    if request.method == "GET":
        return render(request,'edithero.html',{"hero":hero})
    elif request.method == "POST":
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.save()
        url = reverse("booktest:detail",args=(hero.book.id,))
        return redirect(to=url)


def deletehero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    # 一定要先获取在删除
    bookid = hero.book.id
    hero.delete()

    url = reverse("booktest:detail",args=(bookid,))
    return redirect(to=url)


def about(request):
    return HttpResponse("这里是关于")

# 使用django 模板
# MVT
