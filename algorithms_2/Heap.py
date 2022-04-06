class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.heap_size = 0

    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * (2 ** (depth + 1) - 1)
        for heap_elem in a:
            self.Add(heap_elem)

    def GetMax(self):
        heap_array = self.HeapArray
        self.heap_size = self.heap_size - 1
        try:
            if not heap_array or isinstance(heap_array[0], type(None)):
                return -1
            index = heap_array.index(None)
        except:
            index = len(heap_array)

        root_value = heap_array[0]
        heap_array[0] = heap_array[index - 1]
        heap_array[index - 1] = None
        index = 0

        while 2 * index + 2 < self.heap_size and self.HeapArray[index] < max(self.HeapArray[2 * index + 1], self.HeapArray[2 * index + 2]):
            if self.HeapArray[2 * index + 1] > self.HeapArray[2 * index + 2]:
                self.HeapArray[index], self.HeapArray[2 * index + 1] = self.HeapArray[2 * index + 1], self.HeapArray[index]
                index = 2 * index + 1
            else:
                self.HeapArray[index], self.HeapArray[2 * index + 2] = self.HeapArray[2 * index + 2], self.HeapArray[index]
                index = 2 * index + 2
        return root_value

    def Add(self, key):
        heap_array = self.HeapArray
        self.heap_size += 1
        try:
            index = heap_array.index(None)
            heap_array[index] = key
        except:
            return False

        while index > 0 and self.HeapArray[index] > self.HeapArray[(index - 1) // 2]:
            self.HeapArray[index], self.HeapArray[(index - 1) // 2] = self.HeapArray[(index - 1) // 2], self.HeapArray[index]
            index = (index - 1) // 2
        return True




