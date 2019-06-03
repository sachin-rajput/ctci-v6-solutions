class Graph:
    def __init__(self, numOfvertex, undirected = False):
        self.numOfvertex = numOfvertex
        self.undirected = undirected
        self.adjList = [[] for i in range(self.numOfvertex)]

    def addEdge(self, frm, to, cost = 0):
        if to not in self.adjList[frm]:
            self.adjList[frm].append(to)
        
        if self.undirected:
            if frm not in self.adjList[to]:
                self.adjList[to].append(frm)

    
    def printGraph(self):
        for cList in self.adjList:
            print(cList)
    
    def DFS(self):
        visited = [False] * self.numOfvertex

        for i in range(self.numOfvertex):
            if visited[i] == False:
                #helper function
                self.DFSUtil(i, visited)
                print("\n ---- \n")
    
    def DFSUtil(self, s, visited):

        visited[s] = True
        print(s, end=" ")

        for i in self.adjList[s]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    

G = Graph(4)

G.addEdge(0,1)
G.addEdge(0,2)
G.addEdge(1,1)
G.addEdge(1,2)
G.addEdge(3,1)

print(G.adjList)

G.printGraph()

G.DFS()