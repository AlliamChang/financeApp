from flask import Blueprint

app = Blueprint('profile_management',__name__)

from . import views