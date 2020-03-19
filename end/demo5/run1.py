from factory import create_app
from models import *
# 3 启动Web服务
if __name__ == '__main__':
    # 开发环境使用  debug = True自动重启服务器
    app = create_app()
    # db.drop_all()
    # db.create_all()



    app.run(debug=True,host="0.0.0.0")

