# -*- coding: utf-8 -*-
from app import db


class Volunteer(db.Model):
    __tablename__ = 'volunteer'
    volunteerID = db.Column(db.Integer, nullable=False)
    stdNo = db.Column(db.String, nullable=False)
    starttime = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    activity = db.Column(db.String, nullable=False)
    __table_args__ = (
        db.PrimaryKeyConstraint('volunteerID', 'stdNo'),
    )

    def __repr__(self):
        return '<Volunteer %r>' % self.name
