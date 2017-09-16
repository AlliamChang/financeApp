from flask_script import Manager
from app import app
import base64
import urllib
import ssl
import json
import datetime
import hmac
import hashlib

manager = Manager(app)
manager.run()


# def to_md5_base64(strBody):
#     hash = hashlib.md5()
#     hash.update(str(strBody).encode('utf-8'))
#     return hash.hexdigest().encode('base64').strip()
#
#
# def to_sha1_base64(stringToSign, secret):
#     hmacsha1 = hmac.new(secret, stringToSign, hashlib.sha1)
#     return base64.b64encode(hmacsha1.digest())
#
# date = datetime.datetime.strftime(datetime.datetime.utcnow(), "%a, %d %b %Y %H:%M:%S GMT")
# host = 'https://dm-51.data.aliyun.com'
# path = '/rest/160601/ocr/ocr_idcard.json'
# method = 'POST'
# ak_id = '24624153'
# ak_secret = '5ab3dd6cb978b74cb5fcb0735b4745b7'
# url = host + path
#
# file = open("IMG_0278.JPG","rb")
# b64 = base64.b64encode(file.read())
# file.close()
#
# bodys = {
#     "inputs": [
#         {
#             "image": {
#                 "dataType": 50,
#                 "dataValue": b64
#             },
#             "configure": {
#                 "dataType": 50,
#                 "dataValue": {"side": "face"}
#             }
#         }
#     ]
# }
# # bodysmd5 = to_md5_base64(json.dumps(bodys))
# # stringToSign = 'POST'+ '\n' + 'application/json' + '\n' + bodysmd5 + '\n' + 'application/json' + '\n' + date + '\n' + url
# # signature = to_sha1_base64(stringToSign, ak_secret)
# # authHeader = 'Dataplus ' + ak_id + ':' + signature
# data = urllib.parse.urlencode(bodys)
# data = data.encode('utf-8')
# file = open("test.txt", "w")
# file.write(json.dumps(bodys))
# request = urllib.request.Request(url, data)
# request.add_header('Authorization', signature)
# request.add_header('Content-Type', 'application/json; charset=UTF-8')
# request.add_header('date', date)
#
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# response = urllib.request.urlopen(request, context=ctx)
# content = response.read()
# if content:
#     print(content)

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# access_token = '24.da35d3eb776da0b0998c321392992d57.2592000.1508041618.282335-10144452'
# url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/idcard?access_token=' + access_token
# # 二进制方式打开图文件
# f = open('C360_2017-09-15-12-53-18-942.jpg', 'rb')
# # 参数image：图像base64编码
# img = base64.b64encode(f.read())
# params = {"image": img, "id_card_side": "front"}
# params = urllib.parse.urlencode(params)
# # print(params)
# params = params.encode('utf-8')
# # print(params)
# request = urllib.request.Request(url, params)
# request.add_header('Content-Type', 'application/x-www-form-urlencoded')
# response = urllib.request.urlopen(request)
# content = response.read()
# if content:
#     print(content)





