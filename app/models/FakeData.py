#!/usr/bin/python
# -*- coding: UTF-8 -*-

from app import db
from app.models.Progross import Progross
from app.models.Punishment import Punishment
from app.models.Scholarship import Scholarship
from app.models.BankCard import BankCard
from app.models.Volunteer import Volunteer
import datetime


print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
scholarship = Scholarship(scholarID=2, stdNo='151250000', scholarTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          money=2000, type=1)
scholarship2 = Scholarship(scholarID=1, stdNo='151250000', scholarTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                           money=2000, type=1)


volunteer = Volunteer(volunteerID=1, stdNo='151250000', starttime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                      duration=3, activity='羊山公园志愿', volunteercol='活动')
volunteer2 = Volunteer(volunteerID=2, stdNo='151250000', starttime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                       duration=3, activity='羊山公园志愿', volunteercol='活动')

db.session.add(scholarship)
db.session.add(volunteer)
db.session.add(volunteer2)
db.session.add(scholarship2)


db.session.commit()

