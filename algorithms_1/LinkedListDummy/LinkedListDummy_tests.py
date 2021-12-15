from LinkedListDummy import LinkedListDummy, Node
import unittest

class main_tests(unittest.TestCase):
    def list_nodes(self):
        node = self.head_d.next
        nodes_lst = []
        while node is not self.tail_d:
            nodes_lst.append(node.value)
            node = node.next
        return nodes_lst

    def test_add_in_tail(self):
        lld = LinkedListDummy()
        lld.add_in_tail(Node(1))
        self.assertEqual([1], main_tests.list_nodes(lld))

        lld.add_in_tail(Node(2))
        self.assertEqual([1, 2], main_tests.list_nodes(lld))

    def test_add_in_head(self):
        lld = LinkedListDummy()
        lld.add_in_head(Node(1))
        lld.add_in_tail(Node(2))
        self.assertEqual([1, 2], main_tests.list_nodes(lld))

        lld.add_in_head(Node(0))
        self.assertEqual([0, 1, 2], main_tests.list_nodes(lld))

    def test_clean(self):
        lld = LinkedListDummy()
        lld.add_in_tail(Node(1))
        lld.add_in_tail(Node(2))
        lld.add_in_tail(Node(3))
        lld.clean()
        self.assertEqual([], main_tests.list_nodes(lld))

    def test_len(self):
        lld = LinkedListDummy()
        lld.add_in_tail(Node(1))
        lld.add_in_tail(Node(2))
        lld.add_in_tail(Node(3))
        self.assertEqual(lld.len(), 3)

        lld = LinkedListDummy()
        self.assertEqual(lld.len(), 0)

    def test_find(self):
        lld = LinkedListDummy()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        lld.add_in_tail(node_1)
        lld.add_in_tail(node_2)
        lld.add_in_tail(node_3)
        lld.add_in_tail(node_4)
        self.assertEqual(node_2, lld.find(2))
        self.assertEqual(node_4, lld.find(4))

    def test_find_all(self):
        lld = LinkedListDummy()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(1)
        node_4 = Node(4)
        node_5 = Node(1)
        node_6 = Node(5)
        node_7 = Node(1)
        node_8 = Node(4)
        lld.add_in_tail(node_1)
        lld.add_in_tail(node_2)
        lld.add_in_tail(node_3)
        lld.add_in_tail(node_4)
        lld.add_in_tail(node_5)
        lld.add_in_tail(node_6)
        lld.add_in_tail(node_7)
        lld.add_in_tail(node_8)
        nodes = [node_1, node_3, node_5, node_7]
        self.assertEqual(nodes, lld.find_all(1))

    def test_delete_all_false(self):
        lld = LinkedListDummy()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        lld.add_in_tail(node_1)
        lld.add_in_tail(node_2)
        lld.add_in_tail(node_3)
        lld.delete(1)
        self.assertEqual([2, 3], main_tests.list_nodes(lld))
        lld.delete(3)
        self.assertEqual([2], main_tests.list_nodes(lld))
        lld.delete(2)
        self.assertEqual([], main_tests.list_nodes(lld))

        lld.add_in_tail(node_1)
        lld.add_in_tail(node_2)
        lld.add_in_tail(node_3)
        lld.delete(2)
        self.assertEqual([1, 3], main_tests.list_nodes(lld))

    def test_delete_all_true(self):
        lld = LinkedListDummy()
        node_1 = Node(1)
        node_3 = Node(3)

        lld.add_in_tail(node_1)
        lld.add_in_tail(Node(2))
        lld.add_in_tail(Node(2))
        lld.add_in_tail(Node(2))
        lld.add_in_tail(node_3)
        lld.delete(2, True)
        self.assertEqual([1, 3], main_tests.list_nodes(lld))
        lld.clean()

        lld.add_in_tail(node_1)
        lld.add_in_tail(Node(2))
        lld.add_in_tail(Node(2))
        lld.add_in_tail(node_3)
        lld.add_in_tail(Node(2))
        lld.add_in_tail(Node(2))
        lld.add_in_tail(Node(1))
        lld.delete(2, True)
        self.assertEqual([1, 3, 1], main_tests.list_nodes(lld))
        lld.delete(1, True)
        self.assertEqual([3], main_tests.list_nodes(lld))

        lld.add_in_tail(Node(3))
        lld.add_in_tail(Node(3))
        lld.delete(3, True)
        self.assertEqual([], main_tests.list_nodes(lld))

    def test_insert(self):
        lld = LinkedListDummy()
        node_1 = Node(1)
        lld.insert(None, node_1)
        self.assertEqual([1], main_tests.list_nodes(lld))

        node_2 = Node(2)
        lld.add_in_tail(node_2)
        lld.add_in_tail(Node(3))
        lld.insert(None, Node(4))
        self.assertEqual([1, 2, 3, 4], main_tests.list_nodes(lld))

        lld.insert(node_1, Node(5))
        self.assertEqual([1, 5, 2, 3, 4], main_tests.list_nodes(lld))

        lld.insert(node_2, Node(9))
        self.assertEqual([1, 5, 2, 9, 3, 4], main_tests.list_nodes(lld))

if __name__ == '__main__':
    unittest.main()