# encoding:utf-8
from flask import Blueprint

app = Blueprint('check_identity', __name__)

from . import views