# coding:utf8
from . import app
from flask import request
import random
import json

phoneList = {}


@app.route('/sendPhoneCode', methods=['GET'])
def send_phone_code():
    data = {'code': 0, 'message': 'success', 'verifyCode': '0011'}

    return json.dumps(data)


@app.route('/checkPhone', methods=['GET'])
def check_phone():
    data = {'code': 0, 'message': 'true'}

    return json.dumps(data)


@app.route('/checkFace', methods=['POST'])
def check_face():
    data = {'code': 0, 'message': 'success'}

    return json.dumps(data)


@app.route('/checkIdentify', methods=['GET'])
def check_identify():
    data = {'code': 0, 'message': 'success'}

    return json.dumps(data)


@app.route('/getCheckState', methods=['GET'])
def get_check_state():
    data = {'code': 0, 'message': 'success', 'checkstate': 3}

    return json.dumps(data)


@app.route('/getAuthInfo', methods=['GET'])
def get_auth_info():
    data = {'code': 0, 'message': 'success', 'phone': '13012341234', 'name': '小明', 'identifyId': 'success',
            'photo': 'success'}

    return json.dumps(data)
