# -*- coding: utf-8 -*-
from app import db


class Scholarship(db.Model):
    __tablename__ = 'scholarship'
    scholarID = db.Column(db.Integer, nullable=False)
    stdNo = db.Column(db.String, nullable=False)
    scholarTime = db.Column(db.DATE, nullable=False)
    money = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    __table_args__ = (
        db.PrimaryKeyConstraint('scholarID', 'stdNo'),
    )

    def __repr__(self):
        return '<scholarship %r>' % self.name
