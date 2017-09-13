# -*- coding:utf-8 -*-

from . import app
import json

phoneList = {}


@app.route('/getCreditReport', methods=['GET'])
def get_credit_report():
    data = {'code': 0, 'message':'success','idCard': 345245233458759837,'stdNo': 151250000, 'name': '黄小白'
            , 'school': '', 'major': '', 'grade': '', 'gpa': '', 'home': '', 'motherName': '', 'motherIncome': ''
            , 'motherJob': '', 'fatherName': '', 'fatherIncome': '', 'fatherJob': ''
            , 'zhiMaCredit': '', 'consumeRecord': '', 'volunteerRecord': '', 'scholarship': ''
            }
    return json.dumps(data)


@app.route('/getCheckState', methods=['GET'])
def get_check_state():
    data = {'code': 0, 'message': 'success', 'hasBasicAuth': False, 'hasSchoolAuth': True, 'hasBankAuth': True
            , 'hasZhiMaAuth': False, 'hasAllAuth': True
            }
    return json.dumps(data)


@app.route('/confirm_ZhiMaCredit', methods=['GET'])
def confirm_zhima_credit():
    data = {'code': 0, 'message': 'success'}
    return json.dumps(data)