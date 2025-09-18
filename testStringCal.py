import unittest
from stringCal import add

class StringCalTestCases(unittest.TestCase):

    def test_empty_string(self):
        res=add("")
        self.assertEqual(res,0)


    def test_one_num(self):
        res=add("1")
        self.assertEqual(res,1)

    