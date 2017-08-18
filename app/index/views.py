# encoding:utf-8

from . import app
from . import model


@app.route('/user', methods=['GET'])
def get_user():
    user=model.User()
    # print user
    return user.to_json()
