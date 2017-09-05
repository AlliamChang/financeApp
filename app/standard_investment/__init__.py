# -*- coding:utf-8 -*-

from flask import Blueprint

app = Blueprint('standard_investment', __name__)
from . import view
