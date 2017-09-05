# coding:utf8
from . import app
import json

phoneList = {}


@app.route('/fillinBasicInfo', methods=['POST'])
def send_phone_code():
    data = {'code': 0, 'message': 'success'}

    return json.dumps(data)


@app.route('/confirm_ZhiMaCredit', methods=['POST'])
def send_phone_code():
    data = {'code': 0, 'message': 'success'}

    return json.dumps(data)


@app.route('/confirm_BankCredit', methods=['POST'])
def send_phone_code():
    data = {'code': 0, 'message': 'success'}

    return json.dumps(data)


@app.route('/getActivationState', methods=['GET'])
def send_phone_code():
    data = {'code': 0, 'message': 'success', 'verifyCode': '0011', 'ActivationState': 0}

    return json.dumps(data)


@app.route('/getCreditLimit', methods=['GET'])
def send_phone_code():
    data = {'code': 0, 'message': 'success', 'totalLimit': 3, 'surplusLimit': 2}

    return json.dumps(data)
