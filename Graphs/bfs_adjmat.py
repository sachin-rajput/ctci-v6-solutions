class Graph(object):

    def __init__(self, vertices, undirected):
        self.vertices = vertices
        self.undirected = undirected
        self.adjacencyMatrix = [[0 for i in range(self.vertices)] for j in range(self.vertices)]
        self.adjacencyList = [[] for i in range(self.vertices)]

    def addEdgesWithWeight(self, source, destination, weight):
        self.adjacencyMatrix[source][destination] = weight

        if self.undirected:
            self.adjacencyMatrix[destination][source] = weight
    
    def matrixToList(self):
        
        for i, vertex in enumerate(self.adjacencyMatrix):
            adj = []
            for j, connected in enumerate(self.adjacencyMatrix[i]):
                if connected:
                    adj.append(j)
            self.adjacencyList[i] = adj

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

directedGraph = Graph(3, 0)

directedGraph.addEdgesWithWeight(0,0,1)
directedGraph.addEdgesWithWeight(0,1,1)
directedGraph.addEdgesWithWeight(0,2,1)
directedGraph.addEdgesWithWeight(2,0,1)
directedGraph.addEdgesWithWeight(2,1,1)

print(directedGraph.adjacencyMatrix)

directedGraph.matrixToList()

directedGraph.printGraph()

print("\nDirected BFS: ")

directedGraph.BFS(2)


print("\n\nUndirected Graph: ")

undirectedGraph = Graph(3,1)

undirectedGraph.addEdgesWithWeight(0,1,1)
undirectedGraph.addEdgesWithWeight(0,2,1)
undirectedGraph.addEdgesWithWeight(2,1,1)

undirectedGraph.matrixToList()

directedGraph.printGraph()

print("\nUndirected BFS: ")

directedGraph.BFS(2)