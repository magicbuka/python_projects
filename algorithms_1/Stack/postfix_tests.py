import unittest
from postfix import Postfix

class MyTestCase(unittest.TestCase):
    def test_postfix_1(self):
        sourse_string = '12+3*='
        data = Postfix.postfix(sourse_string)
        res = 9
        self.assertEqual( data, res)

    def test_postfix_2(self):
        sourse_string = '12+3*'
        data = Postfix.postfix(sourse_string)
        res = 9
        self.assertEqual( data, res)

    def test_postfix_3(self):
        sourse_string = '85+5*9+='
        data = Postfix.postfix(sourse_string)
        res = 74
        self.assertEqual( data, res)

    def test_postfix_4(self):
        sourse_string = '8 2 + 5 * 9 + =  '
        data = Postfix.postfix(sourse_string)
        res = 59
        self.assertEqual( data, res)

if __name__ == '__main__':
    unittest.main()
