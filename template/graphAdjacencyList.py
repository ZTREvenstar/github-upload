class Vertex:
    def __init__(self, key):
        self.id = key
        # an dict. key is node number, value is weight
        self.neighbors = {}

    def addNeighbor(self, nbr, weight=0):
        self.neighbors[nbr] = weight

    def getNeighbors(self):
        return self.neighbors.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.neighbors[nbr]


class Graph:
    def __init__(self, T=0):
        self.Type = T  # T == 0: undirected graph. T == 1: directed graph
        self.verticesList = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.verticesList.values())

    def __contains__(self, item):
        return item in self.verticesList

    def getSize(self):
        return self.numVertices

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.verticesList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.verticesList:
            return self.verticesList[n]
        else:
            return None

    def addEdge(self, src, dst, weight=1):
        if src not in self.verticesList:
            self.addVertex(src)
        if dst not in self.verticesList:
            self.addVertex(dst)
        self.verticesList[src].addNeighbor(self.verticesList[dst], weight)
        if self.Type == 0:  # for undirected graph
            self.verticesList[dst].addNeighbor(self.verticesList[src], weight)

    def getAllVertices(self):
        return self.verticesList.keys


if __name__ == "__main__":
    g = Graph(0)
    for i in range(6):
        g.addVertex(i)

    # print(g.verticesList)

    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
    for v in g:
        # print(v.getConnections())
        # for w in v.getNeighbors():
        #     print("( %s , %s )" % (v.getId(), w.getId()))

        for w in v.getNeighbors():
            print("( %s , %s , weight == %s )" % (v.getId(), w.getId(), v.getWeight(w)))
