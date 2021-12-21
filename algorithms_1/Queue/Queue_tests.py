import unittest
from Queue import Queue, Queue2Stack

class MyTestCase(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        for i in range(1, 4):
            queue.enqueue(i)
        self.assertEqual(3, queue.size())
        res = []
        while queue.size() > 0:
            res.append(queue.dequeue())
        self.assertEqual([1, 2, 3], res)
        self.assertEqual(0, queue.size())

    def test_rotation(self):
        queue = Queue()
        for i in range(1, 6):
            queue.enqueue(i)
        self.assertEqual(5, queue.size())
        queue.rotation(3)
        self.assertEqual(5, queue.size())
        res = []
        while queue.size() > 0:
            res.append(queue.dequeue())
        self.assertEqual([4, 5, 1, 2, 3], res)

        queue = Queue()
        self.assertEqual(queue, queue.rotation(3))

        queue = Queue()
        for i in range(1, 4):
            queue.enqueue(i)
        self.assertEqual(3, queue.size())
        res = []
        queue.rotation(3)
        while queue.size() > 0:
            res.append(queue.dequeue())
        self.assertEqual([1, 2, 3], res)

        queue = Queue()
        for i in range(1, 3):
            queue.enqueue(i)
        self.assertEqual(2, queue.size())
        queue.rotation(3)
        res = []
        while queue.size() > 0:
            res.append(queue.dequeue())
        self.assertEqual([2, 1], res)

    def test_queue2stack(self):
        queue = Queue2Stack()
        for i in range(1, 4):
            queue.enqueue(i)
        self.assertEqual(3, queue.size())
        res = []
        while queue.size() > 0:
            res.append(queue.dequeue())
        self.assertEqual([1, 2, 3], res)
        self.assertEqual(0, queue.size())

if __name__ == '__main__':
    unittest.main()
