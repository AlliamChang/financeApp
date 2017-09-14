# -*- coding: utf-8 -*-
from app import db


class Progross(db.Model):
    __tablename__ = 'progross'
    phone = db.Column(db.String, nullable=False, primary_key=True)
    hasBasicAuth = db.Column(db.String, nullable=False, default=0)
    hasSchoolAuth = db.Column(db.String, nullable=False, default=0)
    hasBankAuth = db.Column(db.String, nullable=False, default=0)
    hasZhiMaAuth = db.Column(db.String, nullable=False, default=0)
    hasAllAuth = db.Column(db.String, nullable=False, default=0)

    def __repr__(self):
        return '<Progross %r>' % self.name
