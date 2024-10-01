class Graph:
    def __init__(self):
        self.graph={}
    def addvert(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def adjacent(self,vertex,adjacent):
        self.addvert(vertex)
        self.graph[vertex].append(adjacent)
    def vert_adj (self,vertex):
        print(vertex,':',self.graph[vertex])


graph=Graph()

graph.addvert('A')
graph.addvert('B')
graph.addvert('C')
graph.adjacent('d',['a','b'])
graph.vert_adj ('A')
print(graph.graph)