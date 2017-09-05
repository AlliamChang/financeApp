# encoding:utf-8
from flask import Blueprint

app = Blueprint('loan_borrow', __name__)

from . import views