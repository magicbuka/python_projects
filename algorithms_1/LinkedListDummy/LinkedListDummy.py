class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None


class _NodeDummy(Node):
    def __init__(self):
        super().__init__(None)


class LinkedListDummy:
    def __init__(self):
        self.tail_d = _NodeDummy()
        self.head_d = _NodeDummy()
        self.tail_d.prev = self.head_d
        self.head_d.next = self.tail_d

    def find(self, val):
        node = self.head_d.next
        while node is not self.tail_d:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        res = []
        node = self.head_d.next
        while node is not self.tail_d:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def clean(self):
        self.__init__()

    def len(self):
        res = 0
        node = self.head_d
        while node.next is not self.tail_d:
            res += 1
            node = node.next
        return res

    def add_in_tail(self, item):
        prev = self.tail_d.prev
        self.tail_d.prev = item
        self.tail_d.prev.next = self.tail_d
        self.tail_d.prev.prev = prev
        prev.next = self.tail_d.prev

    def add_in_head(self, item):
        next = self.head_d.next
        self.head_d.next = item
        self.head_d.next.next = next
        self.head_d.next.prev = self.head_d
        next.prev = self.head_d.next

    def delete(self, val, all=False):
        node = self.head_d.next
        while node is not self.tail_d:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    break
            node = node.next

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
        else:
            afterNode.next.prev = newNode
            newNode.next = afterNode.next
            afterNode.next = newNode
            newNode.prev = afterNode
