# encoding:utf-8
import unittest
from app.credit.CalculateCreditReport import calculate


class App_test(unittest.TestCase):
    def test_calculate(self):
        calculate("1222222")
