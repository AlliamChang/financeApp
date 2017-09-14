# -*- coding: utf-8 -*-
from app import db


class Progress(db.Model):
    __tablename__ = 'progress'
    phone = db.Column(db.String, nullable=False, primary_key=True)
    hasBasicAuth = db.Column(db.String, nullable=False, default=0)
    hasSchoolAuth = db.Column(db.String, nullable=False, default=0)
    hasBankAuth = db.Column(db.String, nullable=False, default=0)
    hasZhiMaAuth = db.Column(db.String, nullable=False, default=0)
    hasAllAuth = db.Column(db.String, nullable=False, default=0)

    def __repr__(self):
        return '<Progress %r>' % self.name
