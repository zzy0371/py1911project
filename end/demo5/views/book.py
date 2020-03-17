from flask import Blueprint,render_template
bookbp = Blueprint("book",__name__)
@bookbp.route('/')
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
    return render_template("index.html", bl=bookList, u="zzy")