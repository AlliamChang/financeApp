# -*- coding:utf-8 -*-

from . import app
import json
from flask import request
from app.models.User import User
from app.models.Scholarship import Scholarship
from app.models.Volunteer import Volunteer
from app.models.Progross import Progross


@app.route('/getCreditReport', methods=['GET'])
def get_credit_report():

    phone = request.args.get('phone')
    user = User.query.filter_by(phone=phone).first()
    scholarship = Scholarship.query.filter_by(stdNo=user.stdNo)
    volunteer = Volunteer.query.filter_by(stdNo=user.stdNo)
    
    basic_data = [{
        'name': user.name,
        'IDCard': user.idCard,
        'home': user.home,
        'ZhiMaCredit': user.zhiMaCredit,
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

    scholarship_data = []
    for scholar in scholarship:
        scho = {}
        scho['date'] = scholar.scholarTime
        scho['name'] = scholar.type
        scho['cost'] = scholar.money
        scholarship_data.append(scho)

    volunteer_data = []
    for volunteer in volunteer:
        volun_temp = {}
        volun_temp['date'] = volunteer.starttime
        volun_temp['name'] = volunteer.activity
        volun_temp['period'] = volunteer.duration
        volunteer_data.append(volun_temp)

    data = [basic_data, eduInfo_data, scholarship_data, volunteer_data]

    return json.dumps(data, default=str)


@app.route('/getCheckState', methods=['GET'])
def get_check_state():
    data = {}
    phone = request.args.get('phone')
    state = Progross.query.filter_by(phone=phone).first()
    if state is None:
        return 'can not find user'
    else:
        data = {'code': 0, 'message': 'success', 'hasBasicAuth': state.hasBasicAuth, 'hasSchoolAuth': state.hasSchoolAuth, 'hasBankAuth': state.hasBankAuth
                , 'hasZhiMaAuth': state.hasZhiMaAuth, 'hasAllAuth': state.hasAllAuth
                }
    return json.dumps(data)


@app.route('/confirm_ZhiMaCredit', methods=['GET'])
def confirm_zhima_credit():
    data = {'code': 0, 'message': 'success'}
    return json.dumps(data)

