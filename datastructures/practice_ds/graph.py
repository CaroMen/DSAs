class Graph:
    def __init__(self):
        self.adjList = {}

    def add_vertex(self, vertex):
        if not self.adjList[vertex]:
            self.adjList[vertex] = []

    def add_edges(self, src_dest, end_dest):
        self.add_vertex(src_dest)
        self.add_vertex(end_dest)

        self.adjList[src_dest].append(end_dest)
        self.adjList[end_dest].append(src_dest)

    def build_graph(self, edges):
        for edge in edges:
            if len(edge) == 1:
                self.add_edges(edge[0])
            else:
                self.add_edges(edge[0], edge[1])

        return self.adjList

    def bfs(self, vertex):
        queue = [vertex]
        visited = set()
        vertices = []

        while len(queue):
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                continue
            visited.add(current_vertex)
            vertices.append(current_vertex)

            queue.extend(self.adjList[current_vertex])

        return vertices

    def dfs(self, vertex, visited=set(), vertices=[]):
        if vertex in visited:
            return

        visited.add(vertex)
        vertices.append(vertex)

        for neighbor in self.adjList[vertex]:
            self.dfs(neighbor, visited, vertices)

        return vertices
