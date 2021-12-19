import unittest
from braces import Braces

class MyTestCase(unittest.TestCase):
    def test_braces (self):
        sourse_string = '(()'
        data = Braces.braces(sourse_string)
        res = False
        self.assertEqual(data, res)

        sourse_string = '))('
        data = Braces.braces(sourse_string)
        res = False
        self.assertEqual(data, res)

        sourse_string = '))(('
        data = Braces.braces(sourse_string)
        res = False
        self.assertEqual(data, res)

        sourse_string = ')()('
        data = Braces.braces(sourse_string)
        res = False
        self.assertEqual(data, res)

        sourse_string = '(()((())()))'
        data = Braces.braces(sourse_string)
        res = True
        self.assertEqual(data, res)

        sourse_string = '(()()(())'
        data = Braces.braces(sourse_string)
        res = False
        self.assertEqual(data, res)

        sourse_string = '())('
        data = Braces.braces(sourse_string)
        res = False
        self.assertEqual(data, res)

        sourse_string = '((())'
        data = Braces.braces(sourse_string)
        res = False
        self.assertEqual(data, res)

        sourse_string = '(()()()()()()())'
        data = Braces.braces(sourse_string)
        res = True
        self.assertEqual(data, res)

        sourse_string = '((((((((()))))))))'
        data = Braces.braces(sourse_string)
        res = True
        self.assertEqual(data, res)

if __name__ == '__main__':
    unittest.main()
