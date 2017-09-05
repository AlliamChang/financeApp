# encoding:utf-8
from flask import Blueprint

app = Blueprint('activation', __name__)

from . import views