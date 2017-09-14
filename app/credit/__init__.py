# -*- coding:utf-8 -*-

from flask import Blueprint

app = Blueprint('credit', __name__)

from . import BasicInfo
from . import SchoolAuth
from . import CreditReport
