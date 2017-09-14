# -*- coding: utf-8 -*-
from app import db


class Punishment(db.Model):
    __tablename__ = 'punishment'
    stdNo = db.Column(db.String, nullable=False, primary_key=True)
    punishmentcol = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Punishment %r>' % self.name
