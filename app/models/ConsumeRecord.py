# -*- coding: utf-8 -*-
from app import db


class ConsumeRecord(db.Model):
    __tablename__ = 'consumeRecord'
    recordid = db.Column(db.Integer, nullable=False, autoincrement=True)
    bankCard = db.Column(db.String(30), nullable=False)
    consumeTime = db.Column(db.Date, nullable=False)
    money = db.Column(db.Float, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    __table_args__ = (
        db.PrimaryKeyConstraint('recordid', 'bankCard'),
    )

    def __repr__(self):
        return '<ConsumeRecord %r>' % self.name
