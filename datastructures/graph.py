# create a graph

class Graph:
    def __init__(self):
        self.adjList = {}

    def add_vertex(self, vertex):
        if not self.adjList[vertex]:
            self.adjList[vertext] = []

    def add_edges(self, source_value, dest_value):
        self.add_vertex(source_value)
        self.add_vertex(dest_value)

        self.adjList[source_value].append(dest_value)
        self.adjList[dest_value].append(source_value)

    def build_graph(edges):
        for edge in edges:
            if len(edge) == 1:
                self.add_vertex(edge[0])
            else:
                self.add_edges(edge[0], edge[1])

        return self.adjList
