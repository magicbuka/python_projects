class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def __GetAllNodes(self, node):
        if not isinstance(node, type(None)):
            self.counter += 1
            self.__GetAllNodes(node.LeftChild)
            self.__GetAllNodes(node.RightChild)

    def __RedefineRigtLeft(self, delete_node, new):
        parent_node = delete_node.Parent
        if parent_node.LeftChild == delete_node:
            parent_node.LeftChild = new
        else:
            parent_node.RightChild = new

    def __ResetNode(self, node):
        node.Parent = None
        node.LeftChild = None
        node.RightChild = None

    def __WideSearch(self, parent_list=None):
        list_of_nodes = []
        if isinstance(parent_list, type(None)):
            if isinstance(self.Root, type(None)):
                return ()
            list_of_nodes.append(self.Root)
            parent_list = [self.Root]

        children_list = []
        for node in parent_list:
            if not isinstance(node.LeftChild, type(None)):
                children_list.append(node.LeftChild)
            if not isinstance(node.RightChild, type(None)):
                children_list.append(node.RightChild)
        list_of_nodes.extend(children_list)
        if len(children_list) > 0:
            list_of_nodes.extend(self.__WideSearch(children_list))
        return list_of_nodes

    def __DeepSearch(self, current_node, list_of_nodes, order_status):
        # order_status: 0 (in-order), 1 (post-order) и 2 (pre-order)
        if order_status == 0:
            if not isinstance(current_node.LeftChild, type(None)):
                self.__DeepSearch(current_node.LeftChild, list_of_nodes, order_status)
            list_of_nodes.append(current_node)
            if not isinstance(current_node.RightChild, type(None)):
                self.__DeepSearch(current_node.RightChild, list_of_nodes, order_status)
        elif order_status == 1:
            if not isinstance(current_node.LeftChild, type(None)):
                self.__DeepSearch(current_node.LeftChild, list_of_nodes, order_status)
            if not isinstance(current_node.RightChild, type(None)):
                self.__DeepSearch(current_node.RightChild, list_of_nodes, order_status)
            list_of_nodes.append(current_node)
        elif order_status == 2:
            list_of_nodes.append(current_node)
            if not isinstance(current_node.LeftChild, type(None)):
                self.__DeepSearch(current_node.LeftChild, list_of_nodes, order_status)
            if not isinstance(current_node.RightChild, type(None)):
                self.__DeepSearch(current_node.RightChild, list_of_nodes, order_status)

    def FindNodeByKey(self, key):
        find_result_info = BSTFind()
        find_result_info.Node = self.Root

        if isinstance(find_result_info.Node, type(None)):
            find_result_info.Node = None
            return find_result_info

        while find_result_info.Node.NodeKey != key:
            if find_result_info.Node.NodeKey > key:
                if isinstance(find_result_info.Node.LeftChild, type(None)):
                    find_result_info.ToLeft = True
                    break
                find_result_info.Node = find_result_info.Node.LeftChild
            else:
                if isinstance(find_result_info.Node.RightChild, type(None)):
                    break
                find_result_info.Node = find_result_info.Node.RightChild
        else:
            find_result_info.NodeHasKey = True
        return find_result_info

    def AddKeyValue(self, key, val):
        new_node = BSTNode(key, val, None)
        find_result_info = self.FindNodeByKey(key)
        if not find_result_info.NodeHasKey:
            if isinstance(self.Root, type(None)):
                self.Root = new_node
            else:
                new_node.Parent = find_result_info.Node
                if find_result_info.ToLeft:
                    find_result_info.Node.LeftChild = BSTNode(key, val, find_result_info.Node)
                else:
                    find_result_info.Node.RightChild = BSTNode(key, val, find_result_info.Node)
            return True
        else:
            return False

    def FinMinMax(self, FromNode, FindMax):
        if not isinstance(self.Root, type(None)):
            if FindMax:
                while not isinstance(FromNode.RightChild, type(None)):
                    FromNode = FromNode.RightChild
            else:
                while not isinstance(FromNode.LeftChild, type(None)):
                    FromNode = FromNode.LeftChild
        return FromNode

    def DeleteNodeByKey(self, key):
        delete_node = self.FindNodeByKey(key)

        if not delete_node.NodeHasKey:
            return False

        delete_node = delete_node.Node

        if not delete_node.LeftChild and not delete_node.RightChild:
            if not delete_node.Parent:
                self.Root = None 
            else:
                self.__RedefineRigtLeft(delete_node, None)
        else:
            if delete_node.LeftChild and delete_node.RightChild:
                move_node = delete_node.RightChild
                if move_node.LeftChild:
                    move_node = self.FinMinMax(move_node, False)
                    if move_node.RightChild:
                        move_node.RightChild.Parent = move_node.Parent
                        move_node.Parent.LeftChild = move_node.RightChild
                    else:
                        move_node.Parent.LeftChild = None
                    move_node.RightChild = delete_node.RightChild
                    delete_node.RightChild.Parent = move_node
                delete_node.LeftChild.Parent = move_node
                move_node.LeftChild = delete_node.LeftChild
            elif delete_node.RightChild:
                move_node = delete_node.RightChild
            else:
                move_node = delete_node.LeftChild

            if delete_node.Parent:
                move_node.Parent = delete_node.Parent
                self.__RedefineRigtLeft(delete_node, move_node)
            else:
                self.Root = move_node
                move_node.Parent = None

        self.__ResetNode(delete_node)

        return True

    def Count(self):
        self.counter = 0
        self.__GetAllNodes(self.Root)
        return self.counter

    def WideAllNodes(self):
        list_of_nodes = self.__WideSearch()
        return tuple(list_of_nodes)

    def DeepAllNodes(self, order_status):
        # order_status: 0 (in-order), 1 (post-order) и 2 (pre-order)
        if isinstance(self.Root, type(None)):
            return ()
        current_node, list_of_nodes = self.Root, []
        self.__DeepSearch(current_node, list_of_nodes, order_status)
        return tuple(list_of_nodes)

