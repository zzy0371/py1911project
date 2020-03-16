from factory import create_app

# 3 启动Web服务
if __name__ == '__main__':
    # 开发环境使用  debug = True自动重启服务器
    create_app().run()