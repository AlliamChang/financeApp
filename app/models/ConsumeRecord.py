# -*- coding: utf-8 -*-
from app import db


class ConsumeRecord(db.Model):
    __tablename__ = 'consumeRecord'
    recordid = db.Column(db.Integer, primary_key=True)
    bankCard = db.Column(db.String(30), primary_key=True)
    consumeTime = db.Column(db.Date, nullable=False)
    money = db.Column(db.Float, nullable=False)
    type = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Progress %r>' % self.name
