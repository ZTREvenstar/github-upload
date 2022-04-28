from typing import Set


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
    # handle input
    n = int(input())
    myinput = input()
    myinput = myinput.split(" ")

    # initialize the graph
    mygraph = Graph(0)
    for i in range(1, n + 1):
        mygraph.addVertex(i)
    for i in myinput:
        src = int(i[0])
        dst = int(i[2])
        mygraph.addEdge(src, dst)

    # src and dst
    myinput = input()
    myinput = myinput.split(" ")

    SRC = mygraph.getVertex(int(myinput[0]))
    DST = mygraph.getVertex(int(myinput[1]))

    K = int(input())

    solutionNum = [0]

    # 深度优先硬搜， 根深度等于0， 一旦到了目的地，就停止且答案加一， 一旦深度大于了K+1， 就要停止
    # 还需要知道我在的这条路已经访问过了哪些点(传个set)  visited: 在操作这个函数之前哪些点已被访问了
    def dfs(depth: int, V: Vertex, visited: Set):
        if depth > K + 1:
            return
        if V.id == DST.id:
            solutionNum[0] += 1
            return
        visited.add(V)
        for v in V.getNeighbors():
            if v not in visited:
                dfs(depth + 1, v, visited.copy())

    initialSet = set()
    dfs(0, SRC, initialSet)

    print(solutionNum[0])

