"""
Flask - 应用工厂
"""
# 1 引入Flask
from flask import Flask,request,render_template,flash,redirect


def create_app():
    """
    应用工厂负责应用相关所有内容   包括创建  配置
    :return:
    """
    # 2 构建Flask对象 其实就是一个WSGI应用   __name__ 为flask寻找static 以及 templates提供支持
    app = Flask(__name__)

    @app.route('/')
    def index():
        bookList = [
            {
                "ID": 101,
                "Name": "神雕侠侣"
            },
            {
                "ID": 102,
                "Name": "倚天屠龙记"
            },
            {
                "ID": 103,
                "Name": "鹿鼎记"
            },

        ]
        return render_template("index.html", bl=bookList)

    # 注册404 路由自定义错误 页面
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html")

    # 4 绑定路由与视图函数  methods表明当前路由所接受的http方法
    @app.route("/login", methods=["GET", "POST"])
    def login():
        print(request.args.get("name"))
        # 5 在flask中请求对象封装在request中  request代表请求  引入request from flask import requet
        print("登录中的", request, request.method, dir(request))
        if request.method == "GET":
            # 7 使用render_template渲染jinja2模板
            # 模板文件夹和python模块同级
            # 8 静态资源static用法等同template
            # render_template第二个参数为传入模板中的数据
            return render_template("login.html")
        elif request.method == "POST":
            # 6 从form中提取表单参数
            username = request.form.get("username")
            password = request.form.get("password")

            error = None
            if not username:
                error = "用户名必须填写"
            elif not password:
                error = "密码必须填写"

            # 9 使用flash可以将参数传入下一个请求 此处将error写入下一次请求
            if error:
                flash(error, category="error")
                return redirect("/login")
            else:
                return "%s--%s" % (username, password)

    @app.route("/regist", methods=["GET", "POST"])
    def regist():
        if request.method == "GET":
            return render_template("regist.html")
        elif request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            password2 = request.form.get("password2")

            error = None
            if not username:
                error = "用户名不能为空"
            elif not password:
                error = "密码不能为空"
            elif not password2:
                error = "重复密码不能为空"
            elif password != password2:
                error = "密码不一致"
            if error:
                flash(error)
                return redirect("/regist")
            else:
                return "提取注册参数,注册成功"

    # 10 session 是存储在服务器上的加密信息 会将sessionid保存在cookie
    app.secret_key = "\x87\xf04\x92\xa5x0\xa6R\xa2HN2-Y\x81\x87\xb4@*\xea\x19wt"
    return app
