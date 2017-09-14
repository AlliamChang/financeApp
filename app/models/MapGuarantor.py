# -*- coding: utf-8 -*-
from app import db


class MapGuarantor(db.Model):
    __tablename__ = 'mapGuarantor'
    phone = db.Column(db.String, nullable=False, primary_key=True)
    guarantorId = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<MapGuarantor %r>' % self.name
