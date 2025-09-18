import unittest
from stringCal import add

class StringCalTestCases(unittest.TestCase):

    def test_empty_string(self):
        res=add("")
        self.assertEqual(res,0)


    def test_one_num(self):
        res=add("1")
        self.assertEqual(res,1)

    def test_two_nums(self):
        res=add("2,5")
        self.assertEqual(res,7)

    def test_arbitrary_nums(self):
        res=add("1,2,3,4,5,6,7,8,9")
        self.assertEqual(res,45)

    def test_newline_delimeter(self):
        res=add("1,2,3\n4,5,6,7,8\n9")
        self.assertEqual(res,45)

    def test_change_delemeter(self):
        res=add("//;\n1;2;3")
        self.assertEqual(res,6)

    def test_negative_nums(self):
        self.assertRaises(ValueError, add, "1,-2,-3")