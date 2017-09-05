# coding:utf8
from . import app
import json

phoneList = {}


@app.route('/fillinBasicInfo', methods=['POST'])
def fillin_basic_info():
    data = {'code': 0, 'message': 'success'}

    return json.dumps(data)


@app.route('/confirm_ZhiMaCredit', methods=['POST'])
def confirm_ZhiMaCredit():
    data = {'code': 0, 'message': 'success'}

    return json.dumps(data)


@app.route('/confirm_BankCredit', methods=['POST'])
def confirm_BankCredit():
    data = {'code': 0, 'message': 'success'}

    return json.dumps(data)


@app.route('/getActivationState', methods=['GET'])
def get_activation_state():
    data = {'code': 0, 'message': 'success', 'verifyCode': '0011', 'ActivationState': 0}

    return json.dumps(data)


@app.route('/getCreditLimit', methods=['GET'])
def get_credit_limit():
    data = {'code': 0, 'message': 'success', 'totalLimit': 3, 'surplusLimit': 2}

    return json.dumps(data)
