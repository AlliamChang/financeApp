# -*- coding: utf-8 -*-
from app import db


class Scholarship(db.Model):
    __tablename__ = 'scholarship'
    phone = db.Column(db.String, nullable=False, primary_key=True)
    scholarID = db.Column(db.Integer, nullable=False)
    stdNo = db.Column(db.String, nullable=False)
    scholarTime = db.Column(db.DATE, nullable=False)
    money = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<scholarship %r>' % self.name
