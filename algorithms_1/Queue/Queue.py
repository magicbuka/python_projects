from Stack import Stack

class Queue:
    '''
    6.2. меры сложности для операций
    enqueue() - O(1)
    dequeue() - O(n)
    '''

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() != 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

    # 6.3. функция, которая "вращает" очередь по кругу на N элементов
    def rotation(self, N):
        if self.size() != 0:
            for i in range(N):
                self.enqueue(self.dequeue())
        return self


# 6.4. очередь с помощью двух стеков
class Queue2Stack:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if not self.stack2.size():
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def size(self):
        return self.stack1.size() + self.stack2.size()