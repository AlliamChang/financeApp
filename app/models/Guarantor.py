# -*- coding: utf-8 -*-
from app import db


# guaranteeMoney担保人担保额度（千元)  guaranteePercent借款额度（千元）/期限（月）比值
class Guarantor(db.Model):
    __tablename__ = 'guarantor'
    idCard = db.Column(db.String, nullable=False, primary_key=True)
    guaranteeMoney = db.Column(db.INTEGER, nullable=False)
    guaranteePercent = db.Column(db.FLOAT, nullable=False)

    def __repr__(self):
        return '<Guarantor %r>' % self.name
