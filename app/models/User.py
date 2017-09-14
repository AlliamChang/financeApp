# -*- coding: utf-8 -*-
from app import db


class User(db.Model):
    __tablename__ = 'user'
    phone = db.Column(db.String, nullable=False, primary_key=True)
    idCard = db.Column(db.String, nullable=False)
    stdNo = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    school = db.Column(db.String, nullable=False)
    major = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer, nullable=False, default=1)
    gpa = db.Column(db.String, nullable=False, default=0)
    home = db.Column(db.String, nullable=False)
    motherName = db.Column(db.String, nullable=False)
    motherIncome = db.Column(db.Integer, nullable=False, default=0)
    motherJob = db.Column(db.String, nullable=False)
    fatherName = db.Column(db.String, nullable=False)
    fatherIncome = db.Column(db.Integer, nullable=False, default=0)
    fatherJob = db.Column(db.String, nullable=False)
    zhiMaCredit = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name
