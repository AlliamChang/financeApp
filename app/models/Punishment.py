# -*- coding: utf-8 -*-
from app import db


class Punishment(db.Model):
    __tablename__ = 'punishment'
    phone = db.Column(db.String, nullable=False, primary_key=True)
    punishmentLevel = db.Column(db.INTEGER, nullable=False)

    def __repr__(self):
        return '<Punishment %r>' % self.name
