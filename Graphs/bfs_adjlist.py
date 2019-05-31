class Graph(object):

    def __init__(self, vertices, undirected):
        self.vertices = vertices
        self.undirected = undirected
        self.adjacencyList = [[] for i in range(self.vertices)]

    def addEdges(self, source, destination):
        if destination not in self.adjacencyList[source]:
            self.adjacencyList[source].append(destination)
        
        if self.undirected:
            if source not in self.adjacencyList[destination]:
                self.adjacencyList[destination].append(source)

    def printGraph(self):
        for currentList in self.adjacencyList:
            print(currentList)
    

    def BFS(self, s):
        visited = [False] * self.vertices

        queue = []

        queue.insert(0, s)

        visited[s] = True

        while queue:
            s = queue.pop()
            print(s, end=" ")

            for i in self.adjacencyList[s]:
                if visited[i] == False:
                    queue.insert(0, i)
                    visited[i] = True

print("\nDirected Graph: ")

directedGraph = Graph(3,0)

directedGraph.addEdges(0,0)
directedGraph.addEdges(0,1)
directedGraph.addEdges(0,2)
directedGraph.addEdges(2,0)
directedGraph.addEdges(2,1)

directedGraph.printGraph()

print("\nDirected BFS: ")

directedGraph.BFS(2)


print("\n\nUndirected Graph: ")

directedGraph = Graph(3,1)

directedGraph.addEdges(0,1)
directedGraph.addEdges(0,2)
directedGraph.addEdges(2,1)

directedGraph.printGraph()

print("\nUndirected BFS: ")

directedGraph.BFS(2)
