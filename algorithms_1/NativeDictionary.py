class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return sum(bytes(key, encoding='utf-8')) % self.size

    def is_key(self, key):
        if self.slots[self.hash_fun(key)] == key:
            return True
        return False

    def put(self, key, value):
        slot = self.hash_fun(key)
        self.slots[slot] = key
        self.values[slot] = value

    def get(self, key):
        if self.is_key(key):
            return self.values[self.hash_fun(key)]
        return None
