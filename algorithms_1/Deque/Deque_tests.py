import unittest
from Deque import Deque, palindrome

class MyTestCase(unittest.TestCase):

    def test_deque(self):
        deq = Deque()  # [5, 3, 1, 0, 2, 4, 6]
        deq.addFront(0)
        for i in range(1, 6, 2):
            deq.addFront(i)
            deq.addTail(i + 1)
        self.assertEqual(7, deq.size())
        res = []
        count = deq.size()
        while deq.size() > 1:
            res.append(deq.removeTail())
            res.append(deq.removeFront())
            count -= 2
            self.assertEqual(count, deq.size())
        self.assertEqual([6, 5, 4, 3, 2, 1], res)
        self.assertEqual(1, deq.size())
        self.assertEqual(0, deq.removeTail())
        self.assertEqual(None, deq.removeFront())
        self.assertEqual(0, deq.size())

    def test_palindrome(self):
        self.assertEqual(True, palindrome('Анна'))
        self.assertEqual(True, palindrome('А роза упала на лапу Азора'))
        self.assertEqual(False, palindrome('Ан'))
        self.assertEqual(False, palindrome('А роза упала'))
        self.assertEqual(True, palindrome('А'))

if __name__ == '__main__':
    unittest.main()

