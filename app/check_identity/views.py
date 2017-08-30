from . import app
from flask import request
import random
import json

phoneList = {}


@app.route('/sendPhoneCode', methods=['GET'])
def send_phone_code():
    data = {"code": 1, "message": ""}

    phone = request.args.get('phone')
    phone_code = random.randint(1000, 9999)
    phoneList[phone] = phone_code
    data['code'] = 0
    data['message'] = phone_code

    return json.dumps(data)


@app.route('/checkPhone', methods=['GET'])
def check_phone():
    data = {'code': 1, 'message': False}
    phone = request.args.get('phone')
    phone_code = int(request.args.get('verify_code'))
    if phone in phoneList:
        if phoneList[phone]==phone_code:
            data['message']=True

    data['code']=0
    del phoneList[phone]
    return json.dumps(data)

