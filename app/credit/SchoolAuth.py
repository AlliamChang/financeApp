# -*- coding:utf-8 -*-

from . import app
import json

phoneList = {}


@app.route('/academicSystem', methods=['POST'])
def send_phone_code():
    data = {'code': 0, 'message': 'success'}
    return json.dumps(data)
