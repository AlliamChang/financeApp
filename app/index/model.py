# encoding:utf-8
import json


class User:
    # 用于例子
    def to_json(self):
        user = {
            'name': 'Jack',
            'age': 18
        }
        return json.dumps(user)
