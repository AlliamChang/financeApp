# -*- coding: utf-8 -*-
from app import db


class BankCard(db.Model):
    __tablename__ = 'bankCard'
    phone = db.Column(db.String, nullable=False, primary_key=True)
    bankCard = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<BankCard %r>' % self.name
