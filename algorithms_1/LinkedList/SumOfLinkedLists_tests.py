import unittest
from LinkedList import Node, LinkedList
from SumOfLinkedLists import SumEqualLinkedList


class main_tests(unittest.TestCase):
    def list_nodes(self):
        node = self.head
        nodes_lst = []
        while node is not None:
            nodes_lst.append(node.value)
            node = node.next
        return nodes_lst

    def test_equal_contains(self):
        ll1 = LinkedList()
        ll1.add_in_tail(Node(1))
        ll1.add_in_tail(Node(1))
        ll2 = LinkedList()
        ll2.add_in_tail(Node(2))
        ll2.add_in_tail(Node(2))
        sum_res = SumEqualLinkedList(ll1, ll2)
        lst_sum_res = main_tests.list_nodes(sum_res)

        self.assertEqual([3, 3], lst_sum_res)

    def test_nonequal_contains(self):
        ll1 = LinkedList()
        ll1.add_in_tail(Node(1))
        ll1.add_in_tail(Node(1))
        ll2 = LinkedList()
        ll2.add_in_tail(Node(2))
        sum_res = SumEqualLinkedList(ll1, ll2)
        lst_sum_res = main_tests.list_nodes(sum_res)
        self.assertEqual([], lst_sum_res)

    def test_none(self):
        ll1 = LinkedList()
        ll2 = LinkedList()
        sum_res = SumEqualLinkedList(ll1, ll2)
        lst_sum_res = main_tests.list_nodes(sum_res)
        self.assertEqual([], lst_sum_res)

if __name__ == '__main__':
    unittest.main()
