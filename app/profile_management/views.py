from . import app
from flask import request
import json

bank_cards = []


# 得到绑定的银行卡信息
@app.route('/getBankCard', methods=['GET'])
def get_bank_card():
    result = {"code": 0, "message": "", "data": bank_cards}
    return json.dumps(result)


# 添加绑定的银行卡信息
@app.route('/addBankCard', methods=['GET'])
def add_bank_card():
    data = {"card_id": "", "bank_name": ""}
    card_id = request.args.get('bank_card')
    data["card_id"] = card_id
    data["bank_name"] = "中国工商银行"
    bank_cards.append(data)
    result = {"code": 0, "message": "success"}
    return json.dumps(result)


# 用户注册
@app.route('/register', methods=['GET'])
def register():
    result = {"code": 0, "message": "success"}
    return json.dumps(result)


# 用户登录
@app.route('/login', methods=['GET'])
def login():
    result = {"code": 0, "message": "success"}
    return json.dumps(result)


# 获取用户信用报告 该报告在完成激活额度时会生成，在每次完成借贷后会更新
@app.route('/getCreditReport', methods=['GET'])
def get_credit_report():
    result = {"code": 0, "message": "", "user_name": "Jack Ma", "score": 90, "detail": ""}
    return json.dumps(result)