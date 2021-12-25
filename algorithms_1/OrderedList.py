class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc=True):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

    def add(self, value):
        if self.head is None:
            item = Node(value)
            self.head, self.tail = item, item
            item.prev, item.next = None, None
            return
        newNode = Node(value)
        node = self.head
        while node is not None:
            compare_result = OrderedList.compare(self, node.value, value)
            if (compare_result >= 0 and self.__ascending == True) or \
               (compare_result <= 0 and self.__ascending == False):
                if node == self.head:
                    newNode.next = node
                    node.prev, self.head = newNode, newNode
                else:
                    node.prev.next = newNode
                    newNode.prev = node.prev
                    newNode.next = node
                    node.prev = newNode
                return
            elif node == self.tail:
                node.next, self.tail = newNode, newNode
                newNode.prev = node
                return
            node = node.next


    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        if self.head is None:
            return
        while self.head.value == val:
            if self.head.next == None:
                self.__init__()
                return
            self.head = self.head.next
            self.head.prev = None
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
                return

            node = node.next

    def clean(self, asc):
        self.__ascending = asc
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

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.strip() < v2.strip():
            return -1
        elif v1.strip() > v2.strip():
            return 1
        return 0