"""
Flask - 应用工厂
"""
# 1 引入Flask
from flask import Flask,request,render_template,flash,redirect
from views import *

def create_app():
    """
    应用工厂负责应用相关所有内容   包括创建  配置
    :return:
    """
    # 2 构建Flask对象 其实就是一个WSGI应用   __name__ 为flask寻找static 以及 templates提供支持
    app = Flask(__name__)

    # @app.before_first_request
    # def first_request_do_something():
    #     import sqlite3
    #     try:
    #         con = sqlite3.connect("demo5.db")
    #         cur = con.cursor()
    #         cur.execute("DROP TABLE IF EXISTS user;")
    #         cur.execute("CREATE TABLE user (  id INTEGER PRIMARY KEY AUTOINCREMENT,  username TEXT UNIQUE NOT NULL,  password TEXT NOT NULL, create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, is_admin INTEGER DEFAULT 0, is_active INTEGER DEFAULT 1 )")
    #         con.commit()
    #         cur.close()
    #         con.close()
    #     except Exception as e:
    #         print(e)




    # 注册蓝图
    app.register_blueprint(bookbp)
    app.register_blueprint(userbp)
    app.register_blueprint(otherbp)






    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html")

    @app.template_filter()
    def myupperfun(value):
        return value.capitalize()
    # 10 session 是存储在服务器上的加密信息 会将sessionid保存在cookie
    app.secret_key = "\x87\xf04\x92\xa5x0\xa6R\xa2HN2-Y\x81\x87\xb4@*\xea\x19wt"

    app.config["MAIL_SERVER"] = "smtp.163.com"
    app.config["MAIL_PORT"] = 25
    app.config["MAIL_USERNAME"] = "18137128152@163.com"
    app.config["MAIL_PASSWORD"] = "qikuedu"
    app.config['MAIL_DEFAULT_SENDER'] = '老张大讲堂<18137128152@163.com>'

    # 扩展工厂   关联邮件
    mail.init_app(app)

    return app
