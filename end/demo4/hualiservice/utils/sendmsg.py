from urllib import request
from urllib import parse

import urllib.request
import time
import hashlib
import random

from hualiservice.settings import DEBUG

URL = "https://openapi.miaodiyun.com/distributor/sendSMS"
ACCOUNTSID = "5ddd6bfa5d1195eb16d160e64d5dbb8c";
AUTH_TOKEN = "cc8baf390e4f5e8ea9ee4a7df9cbd464";
TEMPLATEID = "241019";
def getCodeStr():
    s = ""
    for i in range(6):
        s += str( random.randrange(0,9))
    return s

class SendMsg:
    def __init__(self,telephone):
        self.telephone = telephone
    def send(self):
        print("python demo starting...")
        to = self.telephone


        if not DEBUG:
            param = getCodeStr();
            t = time.time();
            timestamp = str((int(round(t * 1000))));
            sig = ACCOUNTSID + AUTH_TOKEN + timestamp;
            m1 = hashlib.md5()
            m1.update(sig.encode("utf-8"))
            sig = m1.hexdigest()

            data = "accountSid=" + ACCOUNTSID + "&to=" + to + "&templateid=" + TEMPLATEID + "&param=" + param + "&timestamp=" + timestamp + "&sig=" + sig;
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
            }
            data = str.encode(data);
            req = request.Request(URL, headers=headers, data=data)  # POST方法
            page = request.urlopen(req).read()
            page = page.decode('utf-8')
            print("response from SMS server is:")
            print(page)
            print("python demo finished")
        else:
            param="123456"
        print("发送验证码为", param)
        return param

if __name__ == '__main__':
    try:
        print(SendMsg("15138001200").send())
    except Exception as e:
        print(e)

