# -*- coding:utf-8 -*-

from . import app
import json
from flask import request
from ..models import User
from app import db


@app.route('/getCreditReport', methods=['GET'])
def get_credit_report():

    photo = request.args.get('photo')
    user = User.query.filter_by(photo=photo).first()

    basic_data = [{
        'name': user.name,
        'IDCard': user.IDCard,
        'home': user.home,
        'ZhiMaCredit': user.ZhiMaCredit,
        'father_occupation': user.fatherJob,
        'father_revenue': user.fatherIncome,
        'mother_occupation': user.motherJob,
        'mother_revenue': user.motherIncome,
    }]

    eduInfo_data = [{
        'university': '南京大学',
        'major': user.major,
        'grade': user.grade,
        'schoolNum': user.stdNo,
        'gpa': user.gpa,
    }]





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

