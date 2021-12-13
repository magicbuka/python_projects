class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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

    def delete(self, val, all=False):
        if self.head is None:
            return
        while self.head.value == val:
            if self.head.next == None:
                self.__init__()
                return
            self.head = self.head.next
            self.head.prev = None
            if not all:
                return
        node = self.head
        while self.tail != node:
            if node.next.value == val:
                if node.next.next == None:
                    node.next.prev = None
                    node.next = None
                    self.tail = node
                    return
                node.next.next.prev = node
                node.next = node.next.next
                if not all:
                    return
                continue
            node = node.next

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head, self.tail = newNode, newNode
                newNode.prev, newNode.next = None, None
            else:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail, newNode.prev = newNode, self.tail
        else:
            if self.head is None:
                return None
            elif afterNode == self.tail:
                self.tail = newNode
                afterNode.next = newNode
                newNode.prev = afterNode
                newNode.next = None
            else:
                afterNode.next.prev = newNode
                newNode.next = afterNode.next
                afterNode.next = newNode
                newNode.prev = afterNode

    def add_in_head(self, newNode):
        if self.head is None:
            self.head, self.tail = newNode, newNode
            newNode.prev, newNode.next = None, None
        else:
            curr_node = self.head
            self.head = newNode
            curr_node.prev = self.head
            self.head.next = curr_node
            self.head.prev = None