class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum(value.encode()) % self.size

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        count = 0
        while self.slots[slot] is not None and count < self.size:
            slot += self.step
            count += 1
            if slot >= self.size:
                slot = slot % self.size
        if count != self.size:
            return slot
        return None

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
            return slot
        return None

    def find(self, value):
        for i in range(self.size):
            if self.slots[i] == value:
                return i
        return None