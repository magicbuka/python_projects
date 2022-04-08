class Vertex:

    def __init__(self, val):
        self.Value = val


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

