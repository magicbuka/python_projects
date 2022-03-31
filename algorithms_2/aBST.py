class aBST:

    def __init__(self, depth):
        self.tree_size = 2 ** (depth + 1) - 1 #размер массива
        self.Tree = [None] * self.tree_size  # массив ключей

    def __getLeftChildIndex(self, index):
        return 2 * index + 1

    def __getRightChildIndex(self, index):
        return 2 * index + 2

    def FindKeyIndex(self, key):
        index = 0
        while index < self.tree_size:
            if isinstance(self.Tree[index], type(None)):
                return -index
            elif self.Tree[index] == key:
                return index
            elif key > self.Tree[index]:
                index = self.__getRightChildIndex(index)
            elif key < self.Tree[index]:
                index = self.__getLeftChildIndex(index)
        return None

    def AddKey(self, key):
        # возвращает индекс добавленного/существующего ключа или -1 если не удалось
        index = self.FindKeyIndex(key)
        if not isinstance(index, type(None)):
            index = abs(index)
            self.Tree[index] = key
            return index
        return -1
