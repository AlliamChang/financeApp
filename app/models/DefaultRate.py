# -*- coding: utf-8 -*-
from app import db


#  historyDefault学校历史违约率  defaultMoneyPer学校历史人均违约额
class DefaultRate(db.Model):
    __tablename__ = 'defaultRate'
    school = db.Column(db.String, nullable=False, primary_key=True)
    historyDefault = db.Column(db.FLOAT, nullable=False)
    defaultMoneyPer = db.Column(db.FLOAT, nullable=False)

    def __repr__(self):
        return '<DefaultRate %r>' % self.name
