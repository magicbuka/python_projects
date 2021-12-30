class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.step = 7
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        return sum(bytes(key, encoding='utf-8')) % self.size

    def get_min_hits(self):
        min_value = self.hits[0]
        min_index = 0
        for i in range(1, self.size):
            if self.hits[i] < min_value:
                min_index = i
                min_value = self.hits[i]
        return min_index

    def get_index(self, index):
        return (index + 2) % self.size

    def seek_slot(self, key):
        slot = self.hash_fun(key)
        index = slot
        while self.slots[index] is not None and self.slots[index] != key:
            index = self.get_index(index)
            if index == slot:
                index = self.get_min_hits()
                break
        return index

    def is_key(self, key):
        if self.slots[self.hash_fun(key)] == key:
            return True
        return False

    def put(self, key, value):
        index = self.seek_slot(key)
        self.slots[index] = key
        self.values[index] = value
        self.hits[index] = 0

    def get(self, key):
        slot = self.hash_fun(key)
        index = slot
        while self.slots[index] is not None:
            if self.slots[index] == key:
                self.hits[index] += 1
                return self.values[index]
            index = self.get_index(index)
            if index == slot:
                break
        return None

