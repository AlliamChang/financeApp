# -*- coding:utf-8 -*-
import datetime
from flask import request

from app.models.Progress import Progress
from app.models.User import User
from app.models.Scholarship import Scholarship
from app.models.Volunteer import Volunteer
from . import app
import json
import random
from app import db

homeList = ('上海', '江苏', '浙江', '安徽', '北京', '天津', '广东', '河北', '河南', '山东', '湖北', '湖南', '江西', '福建', '四川', '重庆', '广西', '山西',
            '辽宁', '吉林', '黑龙江', '贵州', '陕西', '云南', '内蒙古', '甘肃', '青海', '宁夏', '新疆', '海南', '西藏', '香港', '澳门', '台湾')
majorList = ('中国语言文学', '数学', '物理学', '天文学', '化学', '计算机科学与技术', '地质学', '生物学')
activity = ('暑假绿植代养活动', '迎新', ' 图书馆、档案馆义工', '志愿者')
moneyList = ('5000', '3000', '2000', '800', '4000')


@app.route('/academicSystem', methods=['POST'])
def defineAcademicSystem():
    data = {'code': 0, 'message': 'success'}
    stdNo = request.args.get('stdNo')
    password = request.args.get('password')
    # stdNo='151250000'
    user = User.query.filter_by(stdNo=stdNo).first()
    phone = user.phone

    if user:
        try:
            user.school = '南京大学'
            user.major = random.choice(majorList)
            user.grade = random.randint(1, 4)
            user.gpa = random.random() + 3.3
            user.home = random.choice(homeList)

            db.session.add(user)

            times1 = random.randint(0, 4)

            for i in xrange(times1):
                year = random.randint(2015, 2017)
                month = random.randint(1, 11)
                day = random.randint(1, 29)

                time = datetime.date(year, month, day)
                lengh = random.randint(1, 10)
                activity1 = random.choice(activity)
                # print "volunteer"
                # print time
                # print lengh
                # print activity1

                volunteer = Volunteer(stdNo=stdNo, starttime=time, duration=lengh, activity=activity1)

                db.session.add(volunteer)

            times2 = random.randint(0, 3)
            for i in xrange(times2):
                year = random.randint(2015, 2017)
                month = random.randint(1, 11)
                day = random.randint(1, 29)

                time = datetime.date(year, month, day)

                type = random.randint(0, 4)

                money = moneyList[type]

                # print "scholarship"
                # print stdNo
                # print time
                # print money
                # print type

                scholarship = Scholarship(stdNo=stdNo, scholarTime=time, money=money, type=type)

                db.session.add(scholarship)

            progress = Progress.query.filter_by(phone=phone).first()

            progress.hasSchoolAuth = 1
            db.session.add(progress)

            db.session.commit()
        except Exception, e:
            print e
            db.session.rollback()
            data['message'] = '网络错误'
            data['code'] = 1

    return json.dumps(data)
