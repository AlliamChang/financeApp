# encoding:utf-8

from . import app
from flask import request
import json


@app.route('/createBit', methods=['post'])
def create_bit():
    data = []
    code = 0
    message = 'xxxx'
    bid_id = 'xxx'
    data['code'] = code
    data['message'] = message
    data['bid_id'] = bid_id

    return json.dumps(data)


@app.route('/finishBit', methods=['post'])
def finish_bit():
    data = []
    code = 0
    message = 'xxxx'
    loan_id = 'xxx'
    end_rate = 6
    data['code'] = code
    data['message'] = message
    data['loan_id'] = loan_id
    data['end_rate'] = end_rate

    return json.dumps(data)


@app.route('/cancelBit', methods=['post'])
def cancel_Bit():
    data = []
    code = 0
    message = 'xxxx'
    data['code'] = code
    data['message'] = message

    return json.dumps(data)


@app.route('/getRateRange', methods=['get'])
def get_rate_range():
    data = []
    code = 0
    start_end = 3
    end_rate = 6
    message = 'xxxx'
    data['code'] = code
    data['message'] = message
    data['start_end'] = 3
    data['end_rate'] = 6

    return json.dumps(data)


@app.route('/getMyBitList', methods=['get'])
def get_my_bit_list():
    data = []
    code = 0
    message = 'xxxx'
    bid_ids = ['xxx', 'xxxx']
    data['code'] = code
    data['message'] = message
    data['bid_ids'] = bid_ids

    return json.dumps(data)


@app.route('/getBitDetail', methods=['GET'])
def get_bit_detail():
    data = []
    code = 0
    message= 'xxxxx'
    bid_id = 'xxx'
    state = 0
    date = 2017 - 8 - 17
    bid_valide_period = 7
    load_duration = 3
    rate = 5
    borrow_style = 0
    usage = ['xxx', 'xxxx']
    repay_style = 0
    money = 20000
    money_has_got = 4000
    progress = 40
    detail = [{'user_id': 'xxxx', 'money': 1000}, {'user_id': 'xxx', 'money': 3000}]

    data['code'] = code
    data['message'] = message
    data['bid_id'] = bid_id
    data['state'] = state
    data['date'] = date
    data['bid_valide_period'] = bid_valide_period
    data['load_duration'] = load_duration
    data['rate'] = rate
    data['borrow_style'] = borrow_style
    data['usage'] = usage
    data[repay_style] = repay_style
    data['money'] = money
    data['money_has_got'] = money_has_got
    data['progress'] = progress
    data['detail'] = detail

    return json.dumps(data)


@app.route('/getAllLoans', methods=['GET'])
def get_all_loans():
    data = []
    code = 0
    message = 'xxxxx'
    loans_id = ['xx', 'xx']

    data['code'] = code
    data['message'] = message
    data['loans_id'] = loans_id

    return json.dumps(data)


@app.route('/getLoanDetail', methods=['GET'])
def get_loan_detail():
    data = []

    code = 0
    message = "xxxx"
    loans_id = "XX"
    state = 0
    money = 10000
    repay_data = 2017-8-28
    repay_money = 5000
    overdue_days = 0
    detail = "xxxx"

    data['code'] = code
    data['loans_id'] = loans_id
    data['message'] = message
    data['state'] = state
    data['money'] = money
    data['repqy_data'] = repay_data
    data['repay_money'] = repay_money
    data['overdue_days'] = overdue_days
    data['detail'] = detail

    return json.dumps(data)


@app.route('repay', methods=['GET'])
def repay():
    data = []
    code = 0
    message = 'xxxxx. '
    data['code'] = code
    data['message'] = message
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

