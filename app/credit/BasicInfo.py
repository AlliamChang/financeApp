# encoding:utf-8

from . import app
from flask import request
import json

verify = '666666'


@app.route('/sendPhoneCode', methods=['POST'])
def send_phone_code():
    phone = request.args.get('phone')

    data = {'code': 0, 'message': 'success', 'verifyCode': verify}
    return json.dumps(data)


@app.route('/checkPhone', methods=['GET'])
def check_phone():
    std_no = request.args.get('stdNo')
    phone = request.args.get('phone')
    verify_code = request.args.get('verifyCode')

    result = 'success'
    if verify != verify_code:
        result = 'wrong'

    data = {'code': 0, 'message': result}
    return json.dumps(data)


@app.route('/checkBasicData', methods=['POST'])
def check_basic_data():
    phone = request.args.get('phone')
    mother_name = request.args.get('motherName')
    mother_income = request.args.get('motherIncome')
    mother_job = request.args.get('motherJob')
    father_name = request.args.get('fatherName')
    father_income = request.args.get('fatherIncome')
    father_job = request.args.get('fatherJob')

    identity_card_photo = request.files['identityCardPhoto']
    face_photo = request.files['facePhoto']

    identity_card_photo.save('identity/' + phone + '.jpg')
    face_photo.save('face/' + phone + '.jpg')

    data = {'code': 0, 'message': 'success'}
    return json.dumps(data)


@app.route('/addBankCard', methods=['POST'])
def add_bank_card():
    std_no = request.args.get('stdNo')
    bank_card = request.args.get('bank_card')

    data = {'code': 0, 'message': 'success'}
    return json.dumps(data)


def confirm_zhi_ma_credit():
    pass


def get_check_state():
    pass
