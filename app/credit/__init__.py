# -*- coding:utf-8 -*-

from flask import Blueprint

app = Blueprint('credit', __name__)

from . import views200

from . import CreditReport
