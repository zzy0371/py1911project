from flask import Blueprint,request,redirect,render_template,flash
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash
userbp = Blueprint("user",__name__)


# 4 绑定路由与视图函数  methods表明当前路由所接受的http方法
@userbp.route("/login", methods=["GET", "POST"])
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
            with sqlite3.connect("demo5.db") as con:
                cur = con.cursor()
                # cur.execute("select * from user where username = ? and password = ?",(username,password))
                cur.execute("select * from user where username = ?",(username,))
                r = cur.fetchall()
                print(r)
                if len(r) <= 0:
                    flash("用户名错误")
                    return redirect("/login")
                else:
                    securityPassword = r[0][2]
                    if not check_password_hash(securityPassword,password):
                        flash("密码错误")
                        return redirect("/login")
                    else:
                        return "%s--%s" % (username, password)




@userbp.route("/regist", methods=["GET", "POST"])
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
            with sqlite3.connect("demo5.db") as con:
                cur = con.cursor()
                cur.execute("select * from user where username = ?", (username,))
                r = cur.fetchall()
                if len(r) > 0:
                    flash("用户已存在")
                    return redirect("/regist")
                else:
                    securityPassword = generate_password_hash(password)
                    cur.execute("insert into user (username, password) values (?,?) ", (username, securityPassword))
                    con.commit()
                    return "提取注册参数,注册成功"





