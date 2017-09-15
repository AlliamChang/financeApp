# encoding:utf-8

from . import app
from flask import request
from app import db
from app.models.Progress import Progress
from app.models.BankCard import BankCard
from app.models.User import User
from app.models.ConsumeRecord import ConsumeRecord
from datetime import *
from sqlalchemy import exc
import random
import os
import json

APIKEY = '5ef620f90b6e812f4b4527a63f973f2c'
msg1 = '【花旗杯】您的验证码是'
msg2 = '。如非本人操作，请忽略本短信'
verify_dict = {}


@app.route('/sendPhoneCode', methods=['POST'])
def send_phone_code():
    phone = request.form['phone']

    verify = make_code()
    # 短信验证
    # smsOperator = SmsOperator(APIKEY)
    # result = smsOperator.single_send({'mobile': '15996259171', 'text': msg1+verify+msg2})
    # print(json.dumps(result.content, ensure_ascii=False))

    if phone and len(phone) == 11:
        verify_dict[phone] = verify
        data = {'code': 0, 'message': 'success', 'verifyCode': verify}
    else:
        data = {'code': 1, 'message': '手机号有误'}
    return json.dumps(data)


@app.route('/checkPhone', methods=['GET'])
def check_phone():
    std_no = request.args.get('stdNo')
    phone = request.args.get('phone')
    verify_code = request.args.get('verifyCode')
    password = request.args.get('password')

    code = 0
    result = 'success'
    if phone and phone in verify_dict:
        if verify_code != verify_dict[phone]:
            result = '验证码错误'
            code = 1
        else:
            del verify_dict[phone]
    else:
        code = 1
        result = '手机号码未申请验证'

    if std_no is None:
        code = 1
        result = '学号未知'

    if code == 0:
        new_user = User(stdNo=std_no, phone=phone, password=password)
        new_progress = Progress(phone=phone)
        try:
            db.session.add(new_user)
            db.session.add(new_progress)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            result = '该手机号已被注册'
            code = 1
        except Exception:
            db.session.rollback()
            result = '网络错误'
            code = 1

    data = {'code': code, 'message': result}
    return json.dumps(data)


@app.route('/checkBasicData', methods=['POST'])
def check_basic_data():
    phone = request.form['phone']
    mother_name = request.form['motherName']
    mother_income = request.form['motherIncome']
    mother_job = request.form['motherJob']
    father_name = request.form['fatherName']
    father_income = request.form['fatherIncome']
    father_job = request.form['fatherJob']
    phone_price = request.form['phonePrice']
    computer_price = request.form['computerPrice']

    identity_card_photo = request.files['identityCardPhoto']
    face_photo = request.files['facePhoto']

    id_dirt = 'identity'
    face_dirt = 'face'
    if not os.path.exists(id_dirt) or not os.path.exists(face_dirt):
        os.makedirs(id_dirt)
        os.makedirs(face_dirt)

    if phone is None:
        code = 1
        result = '缺少电话号码'
    else:
        if identity_card_photo and face_photo:
            identity_card_photo.save('identity/' + str(phone) + '.jpg')
            face_photo.save('face/' + str(phone) + '.jpg')
            code = 0
        else:
            code = 1
            result = '缺少照片'

    if code == 0:
        if mother_job and mother_name and mother_income and father_job and father_income and father_name\
                and computer_price and phone_price:
            code = 0
        else:
            code = 1
            result = '信息不完整'

    if code == 0:
        user = User.query.filter_by(phone=phone).first()
        progress = Progress.query.filter_by(phone=phone).first()
        if user:
            user.motherName = mother_name
            user.motherIncome = mother_income
            user.motherJob = mother_job
            user.fatherName = father_name
            user.fatherIncome = father_income
            user.fatherJob = father_job
            user.computerPrice = computer_price
            user.phonePrice = phone_price

            try:
                db.session.add(user)
                progress.hasBasicAuth = True
                db.session.add(progress)
                db.session.commit()
            except Exception:
                db.session.rollback()
                result = '网络错误'
                code = 1
            else:
                result = 'success'
                code = 0
        else:
            code = 1
            result = '该手机号尚未注册'

    data = {'code': code, 'message': result}
    return json.dumps(data)


@app.route('/addBankCard', methods=['POST'])
def add_bank_card():
    phone = request.form['phone']
    bank_card = request.form['bank_card']

    if phone and bank_card:
        new_bank_card = BankCard(phone=phone, bankCard=bank_card)
        progress = Progress.query.filter_by(phone=phone).first()
        if progress:
            progress.hasBankAuth = True
            try:
                db.session.add(new_bank_card)
                db.session.add(progress)
                db.session.commit()
            except exc.IntegrityError:
                db.session.rollback()
                result = '该号码已绑定过银行卡'
                code = 1
            except Exception:
                db.session.rollback()
                result = '网络错误'
                code = 1
            else:
                result = 'success'
                code = 0
        else:
            code = 1
            result = '不存在该手机号码'
    else:
        code = 1
        result = '缺少信息'

    # 获取银行卡消费记录
    if code == 0:
        flag = random.randint(10, 17)
        get = random.randint(1000, 2000)
        temp = 0
        for i in range(4):
            temp += get
            new_month = ConsumeRecord(id=i, bankCard=bank_card, consumeTime=date.today(), money=get, type=0)
            db.session.add(new_month)
            db.session.commit()

    data = {'code': code, 'message': result}
    return json.dumps(data)


def confirm_zhi_ma_credit():
    pass


def get_check_state():
    pass


def make_code():
    verify = ''
    for i in range(6):
        verify += str(random.randint(0,9))
    return verify
