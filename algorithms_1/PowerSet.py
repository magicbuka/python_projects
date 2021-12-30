class PowerSet:
    def __init__(self):
        self.set = []

    def size(self):
        return len(self.set)

    def put(self, value):
        if value not in self.set:
            self.set.append(value)

    def get(self, value):
        if value in self.set:
            return True
        return False

    def remove(self, value):
        if self.get(value):
            self.set.remove(value)
            return True
        return False

    def intersection(self, set2):
        result_set = PowerSet()
        for i in self.set:
            if set2.get(i):
                result_set.put(i)
        return result_set

    def union(self, set2):
        result_set = PowerSet()
        for i in self.set:
            result_set.put(i)
        for j in set2.set:
            result_set.put(j)
        return result_set

    def difference(self, set2):
        result_set = PowerSet()
        for i in self.set:
            if set2.get(i) is False:
                result_set.put(i)
        return result_set

    def issubset(self, set2):
        for i in set2.set:
            if self.get(i) is False:
                return False
        return True
