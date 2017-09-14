# -*- coding: utf-8 -*-
from app import db


class User(db.Model):
    __tablename__ = 'user'
    phone = db.Column(db.String, primary_key=True)
    idCard = db.Column(db.String, nullable=False, default='')
    stdNo = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False, default='')
    school = db.Column(db.String, nullable=False, default='')
    major = db.Column(db.String, nullable=False, default='')
    grade = db.Column(db.Integer, nullable=False, default=1)
    gpa = db.Column(db.Integer, nullable=False, default=0)
    home = db.Column(db.String, nullable=False, default='')
    motherName = db.Column(db.String, nullable=False, default='')
    motherIncome = db.Column(db.Integer, nullable=False, default=0)
    motherJob = db.Column(db.String, nullable=False, default='')
    fatherName = db.Column(db.String, nullable=False, default='')
    fatherIncome = db.Column(db.Integer, nullable=False, default=0)
    fatherJob = db.Column(db.String, nullable=False, default='')
    zhiMaCredit = db.Column(db.Integer, nullable=False, default=0)
    sex = db.Column(db.Integer, nullable=False, default=0)  # 男0女1
    phonePrice = db.Column(db.Integer, nullable=False, default=0)
    computerPrice = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<User %r>' % self.name
