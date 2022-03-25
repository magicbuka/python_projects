class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []  
        self.level = 0


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def __GetLevels(self, node, node_level_pairs_lst):
        node_level_pairs_lst.append((node.NodeValue, node.level))
        for node in node.Children:
            self.__GetLevels(node, node_level_pairs_lst)
        return node_level_pairs_lst

    def __GetNodes(self, node, nodes_lst):
        nodes_lst.append(node)
        for node in node.Children:
            self.__GetNodes(node, nodes_lst)
        return nodes_lst

    def __FindNodes(self, node, nodes_lst, node_value):
        if node.NodeValue == node_value:
            nodes_lst.append(node)
        for node in node.Children:
            self.__FindNodes(node, nodes_lst, node_value)
        return nodes_lst

    def __GetLeafsCount(self, node, count_leafs):
        if not node.Children:
            count_leafs += 1
        for node in node.Children:
            count_leafs += self.__GetLeafsCount(node, 0)
        return count_leafs

    def AddChild(self, ParentNode, NewChild):
        if isinstance(ParentNode, type(None)):
            ParentNode = self.Root
            self.Root = NewChild
            NewChild.level = 0
        else:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode
            NewChild.level = ParentNode.level + 1

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete is not self.Root:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None

    def GetAllNodes(self):
        nodes_lst = []
        return self.__GetNodes(self.Root, nodes_lst)

    def FindNodesByValue(self, val):
        nodes_lst = []
        return self.__FindNodes(self.Root, nodes_lst, val)

    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        return self.__GetLeafsCount(self.Root, 0)

    def GetNodeLevelPairs(self):
        node_level_pairs_lst = []
        return self.__GetLevels(self.Root, node_level_pairs_lst)




