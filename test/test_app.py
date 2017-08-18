# encoding:utf-8
import unittest
import json
import app


class App_test(unittest.TestCase):
    def setUp(self):
        self.app = app.createApp('testing')
        self.client = self.app.test_client()

    def test_user(self):
        response = self.client.get('/index/user', content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response.get('name') == 'Jack')

