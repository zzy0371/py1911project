"""
WSGI config for bookdemo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 指明django的配置文件为 bookdemo.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookdemo.settings')

application = get_wsgi_application()

# django自带的web服务器   Web Service Gate Interface  网管服务接口
