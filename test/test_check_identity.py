# encoding:utf-8
import unittest
import json
import app


class App_test(unittest.TestCase):
    def setUp(self):
        self.app = app.create_app('testing')
        self.client = self.app.test_client()

    def test_send_phone_code(self):
        response = self.client.get('/check/sendPhoneCode?phone=\'13012341234\'', content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response.get('code') == 0)
        code = int(json_response.get('message'))
        self.assertTrue(code >= 1000 & code <= 9999)

    def test_check_phone(self):
        response = self.client.get('/check/sendPhoneCode?phone=\'13012341234\'', content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        code = int(json_response.get('message'))
        response = self.client.get('/check/checkPhone?phone=\'13012341234\'&verify_code=' + str(code))
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response.get('code') == 0)
        self.assertTrue(json_response.get('message'))
