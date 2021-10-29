#5.1. Самостоятельно разберитесь, как сделать из класса List2 итератор с конструктором, 
# чтобы он работал не только начиная с 1, а с любого заданного значения, например начиная с 5

class List2():
    def __init__(self, start):
        self.start = start
        self.count = 0
        
    def __iter__(self):
        return self

    def __next__(self): 
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if self.count <= 10:
            return current
        raise StopIteration
        
#5.2. Напишите версию List2 с конструктором, который получает количество N итерируемых элементов (сейчас 10), 
# и флажок конечности/бесконечности. В случае конечности List2 выдаёт N элементов и завершает работу, 
# а в случае бесконечности начинает повторно выдавать свою последовательность с самого начала.

class List2():
    def __init__(self, N=10, infinity = False):
        self.start = 1
        self.count = 0
        self.N = N
        self.infinity = infinity
        
    def __iter__(self):
        return self

    def __next__(self): 
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if self.count <= self.N:
            return current
        if self.infinity:
            self.start = 2
            self.count = 1
            return 1
        else:
            raise StopIteration