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

    def bfs(self, starting_vertex):
        visited = set()
        vertices = []
        queue = [starting_vertex]

        while len(queue) > 0:
            current_vertex = queue.pop(0)
            if current_vertex in visited:
                continue
            visited.add(current_vertex)
            vertices.append(current_vertex)

            queue.extend(self.adjList[current_vertex])

        return vertices

    def dfs(self, starting_vertex, visited=set(), vertices=[]):
        if starting_vertex in visited:
            return
        visited.add(starting_vertex)
        vertices.append(starting_vertex)

        for neighbor in self.adjList[starting_vertex]:
            self.dfs(neighbor, visited, vertices)

        return vertices


di = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'c', 'e'],
    'c': ['a', 'b', 'f', 'g'],
    'd': ['a', 'g'],
    'g': ['d', 'c', 'f'],
    'e': ['b'],
    'f': ['c', 'g']
}


edges = [['a', 'b'],
         ['a', 'c'],
         ['a', 'd'],
         ['d', 'g'],
         ['b', 'c'],
         ['b', 'e'],
         ['c', 'f'],
         ['c', 'g'],
         ['f', 'g']]

graph = Graph()

print(graph.build_graph(edges))
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
print(graph.bfs('a'))
print(graph.dfs('a'))
