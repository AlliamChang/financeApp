# -*- coding:utf-8 -*-
from . import app
from flask import request
import json


# 投资人参与标
@app.route('/participateBid',methods=['GET'])
def participate_bid(user_id, bid_id, money):
    data = {"code": 1, "message":"success"}
    return json.dumps(data)


@app.route('/getInvestedBids',methods=['GET'])
# 投资人获取所有的参与标
def get_invested_bids(user_id):
    data = {"code": 1, "message":"success"}
    return json.dumps(data)


@app.route('/getInvestedBidDetail',methods=['GET'])
# 投资人获取参与的标的具体信息
def get_invested_bid_detail(user_id, bid_id):
    data = {"code": 1, "message":"success"}
    return json.dumps(data)


@app.route('/getInvestedLoans',methods=['GET'])
# 投资人获取所有的已经出借的贷款项
def get_invested_loans(user_id):
    data = {"code": 1, "message":"success"}
    return json.dumps(data)


@app.route('/getInvestedLoanDetail',methods=['GET'])
# 投资人获取指定贷款项的具体信息
def get_invested_loan_detail(user_id, loan_id):
    data = {"code": 1, "message":"success"}
    return json.dumps(data)


@app.route('/getAllBidsList',methods=['GET'])
# 获取所有的标的列表，供投资人浏览
def get_all_bids_list(money_range_start, money_range_end, sort_type):
    data = {"code": 1, "message":"success"}
    return json.dumps(data)