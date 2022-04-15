class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size # максимальное количество вершин
        self.m_adjacency = [[0] * size for _ in range(size)] # матрица смежности
        self.vertex = [None] * size # список вершин

    def AddVertex(self, v):
        new_vertex = Vertex(v)
        if None in self.vertex:
            new_vertex_index = self.vertex.index(None)
            self.vertex[new_vertex_index] = new_vertex
            return True
        return False

    def RemoveVertex(self, v):
        # удаление вершины со всеми её рёбрами
        # здесь и далее, параметры v -- индекс вершины
        if v >= self.max_vertex:
            return False
        for v2 in range(len(self.m_adjacency[v])):
            self.RemoveEdge(v, v2)
        self.vertex[v] = None
        return True

    def IsEdge(self, v1, v2):
        # проверка наличия ребра
        # True если есть ребро между вершинами v1 и v2
        if all([v1 < self.max_vertex, v2 < self.max_vertex]):
            return self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1
        return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if all([v1 < self.max_vertex, v2 < self.max_vertex]):
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
            return True
        return False

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if all([v1 < self.max_vertex, v2 < self.max_vertex]):
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0
            return True
        return False

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нет
        vertex_from = self.vertex[VFrom]
        vertex_to = self.vertex[VTo]

        if VFrom == VTo:
            return [vertex_from]
        for v in self.vertex:
            if v:
                v.Hit = False
        stack = []
        current_vertex = VFrom
        while True:
            self.vertex[current_vertex].Hit = True
            stack.append(self.vertex[current_vertex])
            if self.IsEdge(current_vertex, VTo):
                stack.append(vertex_to)
                return stack
            for v in range(self.max_vertex):
                if self.IsEdge(current_vertex, v) and not self.vertex[v].Hit:
                    current_vertex = v
                    break
            else:
                stack.pop()
                if len(stack) == 0:
                    return []
                else:
                    current_vertex = self.vertex.index(stack.pop())

    def BreadthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нет
        vertex_from = self.vertex[VFrom]
        if VFrom == VTo:
            return [vertex_from]
        for v in self.vertex:
            if v:
                v.Hit = False
        queue = []
        parent_array = [None] * self.max_vertex
        queue.append(VFrom)
        vertex_from.Hit = True
        while len(queue) > 0:
            VTo_found = False
            for i in range(self.max_vertex):
                if self.m_adjacency[queue[0]][i] == 1 and self.vertex[i].Hit is False:
                    queue.append(i)
                    self.vertex[i].Hit = True
                    parent_array[i] = queue[0]
                    if i == VTo:
                        VTo_found = True
                        break
            if VTo_found:
                break
            del queue[0]
        if isinstance(parent_array[VTo], type(None)):
            return []
        index = VTo
        result = []
        while not isinstance(index, type(None)):
            result.append(self.vertex[index])
            index = parent_array[index]
        return result[::-1]

