class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def __AddNode(self, parent, a, level=0):
        if a == []:
            return
        array_length = len(a)
        center_index = array_length // 2
        node = BSTNode(a[center_index], parent)
        node.Parent = parent
        node.Level = level
        level += 1
        node.LeftChild = self.__AddNode(node, a[:center_index], level)
        node.RightChild = self.__AddNode(node, a[center_index + 1:], level)
        return node

    def __DepthSubTree(self, node):
        if node is None:
            return 0
        left_depth = self.__DepthSubTree(node.LeftChild)
        right_depth = self.__DepthSubTree(node.RightChild)
        return max(left_depth, right_depth) + 1

    def GenerateTree(self, a):
        array_length = len(a)
        if array_length == 1:
            self.Root = BSTNode(a[0], None)
            return self.Root
        elif isinstance(a, type(None)) or a == []:
            return None
        elif array_length > 1:
            a.sort()
            self.Root = self.__AddNode(None, a)
            return self.Root

    def IsBalanced(self, root_node):
        left = self.__DepthSubTree(root_node.LeftChild)
        right = self.__DepthSubTree(root_node.RightChild)
        return 0 <= abs(left - right) <= 1

