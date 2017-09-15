# encoding:utf-8
import unittest
from app.credit.CalculateCreditReport import judgeZhiMaCredit


class App_test(unittest.TestCase):
    def test_calculate(self):
        print judgeZhiMaCredit(200)
