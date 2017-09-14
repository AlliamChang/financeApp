# encoding:utf-8

from . import db


class Login(db.Model):
    __tablename__ = 'login'
    user_id = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(30), nullable=False)


class BankCard(db.Model):
    __tablename__ = 'bankCard'
    phone = db.Column(db.String(20), primary_key=True)
    bankCard = db.Column(db.String(30), nullable=False)


class User(db.Model):
    __tablename__ = 'user'
    phone = db.Column(db.String(20), primary_key=True)
    idCard = db.Column(db.String(30), default='')
    stdNo = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), default='')
    school = db.Column(db.String(30), default='')
    major = db.Column(db.String(50), default='')
    grade = db.Column(db.Integer, default=1)
    gpa = db.Column(db.String(20), default='')
    home = db.Column(db.String(100), default='')
    motherName = db.Column(db.String(30), default='')
    motherIncome = db.Column(db.Integer, default=0)
    motherJob = db.Column(db.String(30), default='')
    fatherName = db.Column(db.String(30), default='')
    fatherIncome = db.Column(db.Integer, default=0)
    fatherJob = db.Column(db.String(30), default='')
    zhiMaCredit = db.Column(db.Integer, default=0)


class Progress(db.Model):
    phone = db.Column(db.String(20), primary_key=True)
    hasBasicAuth = db.Column(db.Boolean, default=False)
    hasSchoolAuth = db.Column(db.Boolean, default=False)
    hasBankAuth = db.Column(db.Boolean, default=False)
    hasZhiMaAuth = db.Column(db.Boolean, default=False)
    hasAllAuth = db.Column(db.Boolean, default=False)


class LoanInfo(db.Model):
    __tablename__ = 'loan_info'
    loan_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    create_date = db.Column(db.Date, nullable=False)
    loan_money = db.Column(db.Integer, nullable=False)
    remain_money = db.Column(db.Integer, nullable=False)
    bid_valide_period = db.Column(db.Integer, nullable=False)
    loan_duration = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    borrow_style = db.Column(db.Integer, nullable=False)
    usage = db.Column(db.String(255), nullable=False)
    repay_style = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Integer, nullable=False)


class RepayInfo(db.Model):
    __tablename__ = 'repay_info'
    repay_id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, nullable=False)
    repay_user_id = db.Column(db.String(50), nullable=False)
    state = db.Column(db.Integer, nullable=False)
    repay_total = db.Column(db.Float, nullable=False)
    remain_money = db.Column(db.Float, nullable=False)
    next_date = db.Column(db.Date, nullable=False)
    next_repay_money = db.Column(db.Float, nullable=False)
    overdue_day = db.Column(db.Integer, nullable=False)
