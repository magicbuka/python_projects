class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.hash1_code = 17
        self.hash2_code = 223
        self.bit_array = 0

    def _hash(self, str1, hash_code):
        hash_i = 0
        for c in str1:
            code = ord(c)
            hash_i = ((hash_i * hash_code) + code) % self.filter_len
        return 0 | (1 << hash_i)

    def hash1(self, str1):
        return self._hash(str1, self.hash1_code)

    def hash2(self, str1):
        return self._hash(str1, self.hash2_code)

    def add(self, str1):
        self.bit_array |= self.hash1(str1)
        self.bit_array |= self.hash2(str1)

    def is_value(self, str1):
        if self.bit_array & (self.hash1(str1) | self.hash2(str1)) == self.hash1(str1) | self.hash2(str1):
            return True
        return False