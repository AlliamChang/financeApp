# -*- coding: utf-8 -*-
from app import db


class Progress(db.Model):
    __tablename__ = 'progross'
    phone = db.Column(db.String, nullable=False, primary_key=True)
    hasBasicAuth = db.Column(db.Boolean, nullable=False, default=False)
    hasSchoolAuth = db.Column(db.Boolean, nullable=False, default=False)
    hasBankAuth = db.Column(db.Boolean, nullable=False, default=False)
    hasZhiMaAuth = db.Column(db.Boolean, nullable=False, default=False)
    hasAllAuth = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<Progress %r>' % self.name
