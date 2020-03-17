from flask import Blueprint,render_template
otherbp = Blueprint("other",__name__)
# 注册404 路由自定义错误 页面
# @otherbp.errorhandler(404)
# def page_not_found(error):
#     return render_template("404.html")


