# encoding:utf-8
from flask import Blueprint

app=Blueprint('index',__name__)

from . import model,views