class Deque:
    '''
    7.1.
    Как будет различаться мера сложности:
    В текущей реалзации "головой" структуры является нулевой элемент списка.
    addFront - O(n) / removeFront - O(n)
    addTail - O(1) / removeTail - O(1)
    В случае если "голова" будет находиться в другой стороне, ситуация будет обратной
    Почему?
    Операции работы с "хвостом" менее дорогие, чем при работе с "головой"
    т.к. не требуют перемещения других элементов массива.
    '''

    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() != 0:
            return self.deque.pop(0)
        else:
            return None

    def removeTail(self):
        if self.size() != 0:
            return self.deque.pop()
        else:
            return None

    def size(self):
        return len(self.deque)


# 7.2 функция, которая с помощью deque проверяет, является ли некоторая строка палиндромом
def palindrome(s):
    deq = Deque()
    s = s.replace(' ', '').lower()
    for i in s:
        deq.addTail(i)
    for i in range(deq.size() // 2):
        if deq.removeFront() != deq.removeTail():
            return False
    return True