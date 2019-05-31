class Graph:
    def __init__(self, numOfVertex, undirected):
        self.adjMatrix = [[-1] * numOfVertex for x in range(numOfVertex)]
        self.numOfVertex = numOfVertex
        self.undirected = undirected
        self.vertices = {}
        self.verticesList = [0] * numOfVertex
    
    def setVertex(self, index, value):
        if 0 <= index < self.numOfVertex:
            self.vertices[value] = index
            self.verticesList[index] = value
    
    def setEdge(self, frm, to, cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost
        if self.undirected:
            self.adjMatrix[to][frm] = cost

    def getVertex(self):
        return self.verticesList

    def getEdges(self):
        edges = []

        for i in range(self.numOfVertex):
            for j in range(self.numOfVertex):
                if self.adjMatrix[i][j] != -1:
                    edges.append((self.verticesList[i], self.verticesList[j], self.adjMatrix[i][j]))
        
        return edges

    def getMatrix(self):
        return self.adjMatrix

    def matrixToList(self):
        adjList = [[] for x in range(self.numOfVertex)]

        for i in range(self.numOfVertex):
            for j in range(self.numOfVertex):
                if self.adjMatrix[i][j] != -1:
                    adjList[i].append(j)
        
        return adjList

    def BFS(self, s):
        adjList = self.matrixToList()
        
        visited = [False] * self.numOfVertex

        queue = []
        queue.append(s)

        visited[self.vertices[s]] = True
        
        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in adjList[self.vertices[s]]:
                
                if visited[i] == False and i != None:
                    queue.append(self.verticesList[i])
                    visited[i] = True

    def DFS(self, s):
        adjList = self.matrixToList()

        visited = [False] * self.numOfVertex

        self.DFSUtil(s, visited, adjList)

    def DFSComplete(self):
        adjList = self.matrixToList()

        visited = [False] * self.numOfVertex

        for i in range(self.numOfVertex):
            if visited[i] == False:
                self.DFSUtil(self.verticesList[i], visited, adjList)
    
    def DFSUtil(self, s, visited, adjList):

        visited[self.vertices[s]] = True
        print(s, end=" ")

        for i in adjList[self.vertices[s]]:
            if visited[i] == False:
                self.DFSUtil(self.verticesList[i], visited, adjList)

print("\nDirected Graph:")

G = Graph(6, 0)

G.setVertex(0, 'a')
G.setVertex(1, 'c')
G.setVertex(2, 'e')
G.setVertex(3, 'f')
G.setVertex(4, 'g')
G.setVertex(5, 'i')

G.setEdge('a','e',10)
G.setEdge('a','c',20)
G.setEdge('c','g',30)
G.setEdge('i','e',40)
G.setEdge('f','e',60)

print('\nVertices of Graph:')
print(G.getVertex())

print('\nEdges of Graph:')
print(G.getEdges())

print('\nMatrix of Graph:')
print(G.getMatrix())

print('\nBFS of Graph:')
G.BFS('i')

print('\nDFS of Graph:')
G.DFS('i')

print('\nComplete DFS of Graph:')
G.DFSComplete()

print("\n\nUndirected Graph: ")
    
G = Graph(6, 1)

G.setVertex(0, 'a')
G.setVertex(1, 'c')
G.setVertex(2, 'e')
G.setVertex(3, 'f')
G.setVertex(4, 'g')
G.setVertex(5, 'i')

G.setEdge('a','e',10)
G.setEdge('a','c',20)
G.setEdge('c','g',30)
G.setEdge('i','e',40)
G.setEdge('f','e',60)

print('\nVertices of Graph:')
print(G.getVertex())

print('\nEdges of Graph:')
print(G.getEdges())

print('\nMatrix of Graph:')
print(G.getMatrix())

print('\nBFS of Graph:')
G.BFS('a')

print('\nDFS of Graph:')
G.DFS('a')

print('\nComplete DFS of Graph:')
G.DFSComplete()
