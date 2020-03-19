from flask import Blueprint,request,redirect,render_template,flash,current_app
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer,BadSignature,SignatureExpired

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
        email = request.form.get("email")
        password = request.form.get("password")

        error = None
        if not email:
            error = "邮箱必须填写"
        elif not password:
            error = "密码必须填写"

        # 9 使用flash可以将参数传入下一个请求 此处将error写入下一次请求
        if error:
            flash(error, category="error")
            return redirect("/login")
        else:
            with sqlite3.connect("demo5.db") as con:
                cur = con.cursor()
                cur.execute("select * from user where email = ?",(email,))
                r = cur.fetchall()
                print(r)
                if len(r) <= 0:
                    flash("邮箱尚未注册用户")
                    return redirect("/login")
                else:
                    securityPassword = r[0][2]
                    if not check_password_hash(securityPassword,password):
                        flash("密码错误")
                        return redirect("/login")
                    else:
                        if r[0][5] == 0:
                            flash("用户尚未激活不能登录")
                            return redirect("/login")
                        else:
                            return "登录用户  %s" % (email)




@userbp.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        # return "hello"
        return render_template("regist.html")
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        error = None
        if not email:
            error = "邮箱不能为空"
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
                cur.execute("select * from user where email = ?", (email,))
                r = cur.fetchall()
                if len(r) > 0:
                    flash("邮箱已注册")
                    return redirect("/regist")
                else:


                    try:
                        # 需要发送激活链接到用户的邮箱
                        from flask_mail import Message
                        from .utils import mail

                        securityPassword = generate_password_hash(password)
                        cur.execute("insert into user (email, password) values (?,?) ", (email, securityPassword))

                        cur.execute("select id from user where email = ?",(email,))

                        userid = cur.fetchone()[0]
                        print(userid)

                        serUtil = TimedJSONWebSignatureSerializer(current_app.secret_key,expires_in=24*60*60)
                        serstr = serUtil.dumps({"userid":userid}).decode("utf-8")

                        # from tasks import sendmail
                        print("+++")
                        from celery_app import send_mail_async
                        send_mail_async.delay("老张大讲堂激活邮件", email,
                                              "  <a href='http://127.0.0.1:5000/active/%s' >  点击激活  </a> " % (serstr,))

                        # 以上代码都没有错误才进行提交
                        # con.commit()


                        return "提取注册参数,注册成功"
                    except Exception as e:
                        print(e)
                        con.rollback()
                        return "出异常了"




@userbp.route("/active/<userid>")
def activeuser(userid):
    try:
        serUtil = TimedJSONWebSignatureSerializer(current_app.secret_key,expires_in=24*60*60)
        userid = serUtil.loads(userid)["userid"]
        with sqlite3.connect("demo5.db") as con:
            cur = con.cursor()
            cur.execute("update user set is_active = 1 where id = ?", (userid,))
            con.commit()
        return redirect("/login")
    except SignatureExpired:
        return "超时了"
    except BadSignature:
        return "秘钥错误"
    except Exception:
        return "位置原因导致激活失败"





