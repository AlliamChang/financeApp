# encoding:utf-8

from . import app
# from yunpian.SmsOperator import SmsOperator
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
msg1 = '【未来信】您的验证码是'
msg2 = '。如非本人操作，请忽略本短信'
verify_dict = {}


@app.route('/login', methods=['POST'])
def login():
    phone = request.form['phone']
    pwd = request.form['password']
    user = User.query.filter_by(phone=phone).first()

    if user is None:
        data = {'code': 1, 'message': '该账号未注册'}
    elif user.password == pwd:
        data = {'code': 0, 'message': 'success'}
    elif user.password != pwd:
        data = {'code': 1, 'message': '密码错误'}
    else:
        data = {'code': 1, 'message': '登录失败'}
    return json.dumps(data)


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


@app.route('/checkPhone', methods=['POST'])
def check_phone():
    std_no = request.values.get('stdNo')
    phone = request.values.get('phone')
    verify_code = request.values.get('verifyCode')
    password = request.values.get('password')

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
        if mother_job and mother_name and mother_income and father_job and father_income and father_name:
            code = 0
        else:
            code = 1
            result = '信息不完整'

    if code == 0:
        user = User.query.filter_by(phone=phone).first()
        progress = Progress.query.filter_by(phone=phone).first()
        if user:
            user.name = "张三"
            user.idCard = "320322199230409340"
            user.motherName = mother_name
            user.motherIncome = mother_income
            user.motherJob = mother_job
            user.fatherName = father_name
            user.fatherIncome = father_income
            user.fatherJob = father_job
            user.computerPrice = 0
            user.phonePrice = 0
            user.sex = random.randint(0, 1)
            user.age = random.randint(17, 27)

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
    phone = request.values.get('phone')
    bank_card = request.values.get('bank_card')

    if phone and bank_card:
        new_bank_card = BankCard(phone=phone, bankCard=bank_card)
        progress = Progress.query.filter_by(phone=phone).first()
        if progress:
            try:
                db.session.add(new_bank_card)
                # 获取银行卡消费记录
                code = get_bank_record(bank_card)
                if code == 0:
                    progress.hasBankAuth = True
                    db.session.add(progress)
                    db.session.commit()
                    result = 'success'
                else:
                    code = 1
                    result = '添加银行记录失败'
            except exc.IntegrityError:
                code = 1
                db.session.rollback()
                result = '该账号已添加过银行卡'
            except Exception as e:
                print(e)
                db.session.rollback()
                result = '网络错误'
                code = 1
        else:
            code = 1
            result = '不存在该手机号码'
    else:
        code = 1
        result = '缺少信息'

    data = {'code': code, 'message': result}
    return json.dumps(data)


def get_bank_record(bank_card):
    code = 0
    all = 0
    month = random.randint(1000, 2000)
    try:
        for i in range(4):
            all += month
            new_month = ConsumeRecord(bankCard=bank_card, consumeTime=date.today(), money=month, type=0)
            db.session.add(new_month)
            for j in range(random.randint(2,5)):
                if all == 0:
                    break
                type = random.randint(1, 2)
                if type == 2:
                    if all < 400:
                        cost = random.randint(100, all)
                    else:
                        cost = random.randint(100, 400)
                else:
                    if all < 300:
                        cost = random.randint(0, all)
                    else:
                        cost = random.randint(0, 300)
                all -= cost
                new_cost = ConsumeRecord(bankCard=bank_card, consumeTime=date.today(), money=cost, type=type)
                db.session.add(new_cost)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        code = 1

    return code


def make_code():
    verify = ''
    for i in range(6):
        verify += str(random.randint(0, 9))
    return verify

