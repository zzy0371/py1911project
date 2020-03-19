from flask import Blueprint,render_template
from models.book import *
bookbp = Blueprint("book",__name__)
@bookbp.route('/')
def index():
    # c = Category()
    # c.name="武侠"
    # db.session.add(c)
    #
    # c1 = Category()
    # c1.name="科幻"
    # db.session.add(c1)
    #
    #
    # c2 = Category()
    # c2.name="玄幻"
    # db.session.add(c2)
    #
    #
    # c3 = Category()
    # c3.name="言情"
    # db.session.add(c3)
    #
    #
    # db.session.commit()



    cs = Category.query.all()
    return render_template("index.html", cs=cs)



@bookbp.route("/categorys/<id>")
def category(id):
    c = Category.query.filter_by(id=id).first()

    if c:
        # 表关联查询
        # bs = Book.query.filter_by(cid=c.id).all()
        # bs[0].cid

        # 关系字段查询
        bs = c.books
        print(bs[0].category.id,bs[0].category.name)
        return render_template("category.html",bs = bs)
    return "输入不合法"