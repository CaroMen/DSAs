# create a graph

class Graph:
    def __init__(self):
        self.adjList = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []

    def add_edges(self, source_value, dest_value):
        self.add_vertex(source_value)
        self.add_vertex(dest_value)

        self.adjList[source_value].append(dest_value)
        self.adjList[dest_value].append(source_value)
        # print(self.adjList)

    def build_graph(self, edges):
        for edge in edges:
            if len(edge) == 1:
                self.add_vertex(edge[0])
            else:
                self.add_edges(edge[0], edge[1])

        return self.adjList


edgesa = [['a', 'b'],
          ['c']]
#   ['a', 'd'],
#   ['d', 'g'],
#   ['b', 'c'],
#   ['b', 'e'],
#   ['c', 'f'],
#   ['c', 'g'],
#   ['f', 'g']]

graph = Graph()

print(graph.build_graph(edgesa))
"""
{
    'a': ['b', 'c', 'd'],
    'b': ['a', 'c', 'e'],
    'c': ['a', 'b', 'f', 'g'],
    'd': ['a', 'g'],
    'g': ['d', 'c', 'f'],
    'e': ['b'],
    'f': ['c', 'g']}

"""
