# -*- coding:utf-8 -*-

from app.models.User import User
from app.models.Scholarship import Scholarship
from app.models.Volunteer import Volunteer
from app.models.Punishment import Punishment
from app.models.ConsumeRecord import ConsumeRecord
from app.models.BankCard import BankCard
from app.models.Guarantor import Guarantor
from app.models.MapGuarantor import MapGuarantor
from app.models.DefaultRate import DefaultRate
import random


def random_index(rate):
    """随机变量的概率函数"""
    start = 0
    randnum = random.randint(1, sum(rate))

    for index, item in enumerate(rate):
        start += item
        if randnum <= start:
            break
    return index


def judgeSex(sex):
    if sex == 0:
        return 3
    else:
        return 4


# 判断年龄 未成年：-1	 18-21：0	21+：1
def judgeAge(age):
    if age < 18:
        return -1
    elif 18 <= age <= 21:
        return 0
    else:
        return 1


# 判断学校 985 4	 211 3	 一般一本 2	 其他 1
def judgeSchool(school):
    flag = [4, 3, 2, 1]
    return flag[random_index([10, 20, 40, 30])]


# 判断专业 热门 6	 一般 4	冷门 2
def judgeMajor(major):
    flag = [6, 4, 2]
    return flag[random_index([50, 30, 20])]


# 判断成绩 优秀 9	良好 7	中等 5	较差 3	差 1
def judgeGpa(gpa):
    flag = [9, 7, 5, 3, 1]
    return flag[random_index([10, 20, 45, 20, 5])]


# 判断奖学金类型 国奖/校级 7	一等 5 	二等 3	三等 2 无 0
def judgeScholarshipType(scholarship):
    flag = [7, 5, 3, 2, 0]
    return flag[random_index([3, 7, 15, 25, 50])]


# 判断月生活费水平／千元
def judgeLivingCost(bank_card):
    consume_record = ConsumeRecord.query.filter_by(bankCard=bank_card.bankCard).all()
    flag = [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0]
    return flag[random_index([2, 10, 15, 20, 35, 10, 5, 3])]


# 判断奖助学金/学年／千元
def judgeScholarshipNum(scholarship):
    flag = [3, 4, 5, 6, 7, 8, 9]
    return flag[random_index([2, 10, 15, 20, 35, 10, 5, 3])]


# 判断兼职/月／千元
def judgePartTimeIncome(phone):
    flag = [0.3, 0.5, 0.7, 0.9, 1.2, 1.5]
    return flag[random_index([2, 10, 15, 20, 35, 10, 5, 3])]


# 判断生源地gdp/万元
def judgeHomeGdp(home):
    flag = [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0]
    return flag[random_index([2, 10, 15, 20, 35, 10, 5, 3])]


# 判断处分情况 警告：-1	记过：-2	留校察看：-3	开除：-4
def judgePunishment(punishment):
    flag = [0, -1, -2, -3, -4]
    return flag[random_index([80, 10, 5, 3, 2])]


# 判断志愿时长 无：0	0-10：1	 10-20：2	 20+：3
def judgeVolunteer(volunteer):
    flag = [0, 1, 2, 3]
    return flag[random_index([10, 20, 50, 20])]


# 判断芝麻信用   较差：-4	中等：-2	良好：0	优秀：2	极好：4
def judgeZhiMaCredit(zhima):
    flag = [-4, -2, 0, 2, 4]
    return flag[random_index([5, 20, 55, 20])]


def percentNormalize(percent):
    return 100 - percent * 100


def dataNormalize(data):
    return 100 - data * 0.2


def calculate(phone):
    data = []
    user = User.query.filter_by(phone=phone).first()
    volunteer = Volunteer.query.filter_by(stdNo=user.stdNo).all()
    scholarship = Scholarship.query.filter_by(stdNo=user.stdNo).all()
    punishment = Punishment.query.filter_by(phone=phone).all()

    bank_card = BankCard.query.filter_by(phone=phone).all()

    map_guarantor = MapGuarantor.query.filter_by(phone=phone).first()
    guarantor = Guarantor.query.filter_by(idCard=user.idCard).all()

    default_rate = DefaultRate.query.filter_by(school=user.school).first()

    # if (user is None) or (volunteer is None) or (scholarship is None) or (punishment is None) or (
    #             bank_card is None) or (map_guarantor is None) or (guarantor is None) or (default_rate is None):
    #     return None

    data[0] = judgeSex(user.sex)
    # 年龄 身份证那边获取
    # data[1] = judgeAge(age)
    # 学历 教务网那边获取
    # data[2] = user.education
    data[3] = judgeSchool(user.school)
    data[4] = judgeMajor(user.major)
    data[5] = judgeGpa(user.gpa)
    data[6] = judgeScholarshipType(scholarship)
    data[7] = judgeLivingCost(bank_card)
    data[8] = judgeScholarshipNum(scholarship)
    data[9] = judgePartTimeIncome(phone)
    data[10] = float(user.phonePrice + user.computerPrice) / 1000
    data[11] = float(user.motherIncome + user.fatherIncome) / 10000
    data[12] = judgeHomeGdp(user.home)
    data[13] = percentNormalize(default_rate.historyDefault)
    data[14] = dataNormalize(default_rate.guaranteePercent)
    data[15] = judgePunishment(punishment)
    data[16] = judgeVolunteer(volunteer)
    # 担保人担保额度（千元）（1）
    data[17] = float(guarantor.guaranteeMoney) / 1000
    # 借款额度（千元）/期限（月）比值（1）
    data[18] = guarantor.guaranteePercent
    data[19] = judgeZhiMaCredit(user.zhiMaCredit)
    # return data
    net(data)


# 神经网络计算违约概率 然后转换为额度
def net(data):
    return round(random.uniform(1, 10), 2)
