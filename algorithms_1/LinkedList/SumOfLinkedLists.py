from LinkedList import LinkedList, Node

def SumEqualLinkedList(linkedlist1, linkedlist2):
    linkedlist_res = LinkedList()
    if linkedlist1.len() == linkedlist2.len():
        node1, node2 = linkedlist1.head, linkedlist2.head
        while node1 is not None:
            linkedlist_res.add_in_tail(Node(node1.value + node2.value))
            node1, node2 = node1.next, node2.next
    return linkedlist_res