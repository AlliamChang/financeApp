from . import app
from flask import request
import json

bid_list = []


# 投资人参与标
@app.route('/participateBid',methods=['GET'])
def participate_bid():
    data = {"code": 0, "message": "success"}
    bid_id = request.args.get('bid')
    bid_list.append(bid_id)
    return json.dumps(data)


# 投资人获取所有的参与标
@app.route('/getInvestedBids',methods=['GET'])
def get_invested_bids():
    data = {"code": 0, "message": "all", "bid_id":bid_list}
    return json.dumps(data)


# 投资人获取参与的标的具体信息
@app.route('/getInvestedBidDetail',methods=['GET'])
def get_invested_bid_detail():
    bid_id = request.args.get('bid')
    if bid_id in bid_list:
        data = {"code": 0, "message": "success", "bid_id": bid_id, "investmoney": 1000}
    else:
        data = {"code": 1, "message": "not existed"}
    return json.dumps(data)


# 投资人获取所有的已经出借的贷款项
@app.route('/getInvestedLoans',methods=['GET'])
def get_invested_loans():
    user_id = request.args.get('user_id')
    data = {"code": 0, "message": user_id, "loanIDs": [1,2,3]}
    return json.dumps(data)


# 投资人获取指定贷款项的具体信息
@app.route('/getInvestedLoanDetail',methods=['GET'])
def get_invested_loan_detail():
    loan_id = request.args.get('loan_id')
    data = {"code": 0, "message": loan_id, "borrower_id": 123, "state": 0, "money": 1000, "repay_date": "2017-09-30", "repay_money": 500, "overdue_days": 0}
    return json.dumps(data)


# 获取所有的标的列表，供投资人浏览
@app.route('/getAllBidsList',methods=['GET'])
def get_all_bids_list():
    data = {"code": 0, "message": "success", "bid_ids": [1,2,3,4,5,6,7,8,9]}
    return json.dumps(data)