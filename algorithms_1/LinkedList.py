class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        res = []
        node = self.head
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all=False):
        if self.head is None:
            return

        while self.head.value == val:
            if self.head.next == None:
                self.__init__()
                return
            self.head = self.head.next
            if not all:
                return

        node = self.head
        while self.tail != node:
            if node.next.value == val:
                if node.next.next == None:
                    node.next = None
                    self.tail = node
                    return
                node.next = node.next.next
                if not all:
                    return
                continue
            node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        if self.head is None:
            return 0
        res = 1
        node = self.head
        while node.next is not None:
            res += 1
            node = node.next
        return res

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.head = newNode
            return

        newNode.next = afterNode.next
        afterNode.next = newNode
