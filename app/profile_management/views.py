# encoding:utf-8

from . import app
from flask import request
from app import db
from app import model
from sqlalchemy import exc
import json
import random


__bank_name = ["中国农业银行","中国工商银行","中国建设银行","中国银行","广发银行","中国人民银行","中信银行"]


# 得到绑定的银行卡信息
@app.route('/getBankCard', methods=['GET'])
def get_bank_card():
    user_id = request.args.get('user_id')
    bank_cards = model.BankCard.query.filter_by(user_id=user_id).all()

    data = []
    for bank_card in bank_cards:
        each = {"bank_card_num": bank_card.bank_card_number, "bank_name": bank_card.description}
        data.append(each)
    result = {"code": 0, "message": user_id, "data": data}
    return json.dumps(result)


# 添加绑定的银行卡信息
@app.route('/addBankCard', methods=['POST'])
def add_bank_card():
    user_id = request.args.get('user_id')
    card_num = request.args.get('card_num')

    bank_card = model.BankCard(user_id=user_id, bank_card_number=card_num,
                               description=__bank_name[random.randint(0,len(__bank_name))-1])
    db.session.add(bank_card)
    db.session.commit()
    result = {"code": 0, "message": bank_card.description}
    return json.dumps(result)


# 用户注册
@app.route('/register', methods=['POST'])
def register():
    user_id = request.args.get('user_id')
    password = request.args.get('password')

    new_user = model.Login(user_id=user_id, password=password)
    code = 1
    try:
        db.session.add(new_user)
        db.session.commit()
    except exc.IntegrityError:
        db.session.rollback()
        msg = "user id was existed"
    except Exception:
        msg = "unknown error"
    else:
        msg = "success"
        code = 0
    result = {"code": code, "message": msg}
    return json.dumps(result)


# 用户登录
@app.route('/login', methods=['GET'])
def login():
    user_id = request.args.get('user_id')
    password = request.args.get('password')

    user = model.Login.query.filter_by(user_id=user_id, password=password).first()
    if user == None:
        result = {"code": 1, "message": "failed"}
    else:
        result = {"code": 0, "message": "success"}
    return json.dumps(result)


# 获取用户信用报告 该报告在完成激活额度时会生成，在每次完成借贷后会更新
@app.route('/getCreditReport', methods=['GET'])
def get_credit_report():
    user_id = request.args.get('user_id')

    result = {"code": 0, "message": "", "user_name": "Jack Ma", "score": 90, "detail": ""}
    return json.dumps(result)
