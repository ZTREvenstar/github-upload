# redefine place
A = 0  # Arad
B = 1  # Bucharest
C = 2  # Craiova
D = 3  # Dobreta
E = 4  # Eforie
F = 5  # Fagaras
G = 6  # Giurgiu
H = 7  # Hirsova
I = 8  # Iasi
L = 9  # Lugoj
M = 10  # Mehadia
N = 11  # Neamt
O = 12  # Oradea
P = 13  # Pitesti
R = 14  # Rimnicu Vilcea
S = 15  # Sibiu
T = 16  # Timisoara
U = 17  # Urziceni
V = 18  # Vaslui
Z = 19  # Zerind

N = 20


class Graph:  # 寻路问题的Graph一般都比较dense？ 所以用了matrix
    def __init__(self):
        self.graphMatrix = [[0] * N for _ in range(N)]

    def addEdge(self, src, dst, weight=1):
        if src < N:
            if dst < N:
                self.graphMatrix[src][dst] = weight
                self.graphMatrix[dst][src] = weight

    def getEdgeWeight(self, src, dst):
        return self.graphMatrix[src][dst]


class PriorityQueue:  # 暴力方法实现get最小，不是堆

    def __init__(self):
        self.queue = []

    def put(self, node_cost):
        """
        :param node_cost: [node_id,cost]  it is a list of length 2
        """
        self.queue.append(node_cost)

    def getMin(self):  # 暴力遍历get最小 已执行pop
        if self.queue:
            min_index = 0
            min_cost = self.queue[min_index][1]
            for i in range(len(self.queue)):
                if self.queue[i][1] < min_cost:
                    min_index = i
                    min_cost = self.queue[i][1]
            return self.queue.pop(min_index)

    def contain(self, value):  # 暴力遍历
        for i in range(len(self.queue)):
            if self.queue[i][0] == value:
                return self.queue[i], True
        return None, False

    def isEmpty(self):
        if self.queue:
            return False
        return True


def A_star(graph, hFunc, src, dst):

    parents = [0] * N  # used to record the path
    Frontier = PriorityQueue()
    Visited = []

    Frontier.put([src, 0])

    while not Frontier.isEmpty():

        # walk to the node in Frontier with smallest F
        current = Frontier.getMin()
        currentNode = current[0]
        currentF = current[1]

        if currentNode == dst:
            break

        Visited.append(currentNode)

        for childNum in range(N):  # for all outgoing edges of parent
            w = graph.getEdgeWeight(currentNode, childNum)
            if w == 0:
                continue
            if childNum in Visited:
                continue

            node, result = Frontier.contain(childNum)
            childF = currentF - hFunc[currentNode]  # this is current g(n)
            childF += w + hFunc[childNum]

            if result:  # i exists in Frontier set
                oldF = node[1]
                if oldF > childF:  # use new childF to replace oldF
                    node.pop()
                    parents[childNum] = currentNode
                    Frontier.put([childNum, childF])
            else:  # i does not exist in Unvisited, insert child
                parents[childNum] = currentNode
                Frontier.put([childNum, childF])

    dstPath = []
    node = dst
    cost = 0
    while node != src:
        cost += graph.getEdgeWeight(parents[node], node)
        dstPath.append(node)
        node = parents[node]
    dstPath.append(src)
    dstPath.reverse()
    return cost, dstPath


def init_graph():
    graph = Graph()

    graph.addEdge(O, Z, 71)
    graph.addEdge(O, S, 151)
    graph.addEdge(A, Z, 75)
    graph.addEdge(A, S, 140)
    graph.addEdge(A, T, 118)
    graph.addEdge(T, L, 111)
    graph.addEdge(L, M, 70)
    graph.addEdge(M, D, 75)
    graph.addEdge(D, C, 120)
    graph.addEdge(S, R, 80)
    graph.addEdge(S, F, 99)
    graph.addEdge(R, C, 146)
    graph.addEdge(F, B, 211)
    graph.addEdge(R, P, 97)
    graph.addEdge(C, P, 138)
    graph.addEdge(P, B, 101)
    graph.addEdge(B, G, 90)
    graph.addEdge(B, U, 85)
    graph.addEdge(U, H, 98)
    graph.addEdge(U, V, 142)
    graph.addEdge(V, I, 92)
    graph.addEdge(I, N, 87)
    graph.addEdge(H, E, 86)

    return graph


if __name__ == '__main__':

    graph = init_graph()

    h = (366, 0, 160, 242, 161,
         178, 77, 151, 226, 244,
         241, 234, 380, 98, 193,
         253, 329, 80, 199, 374)

    # place_str = input()
    # places = place_str.split()
    # cost = a_star(graph, h, eval(places[0]), eval(places[1]))

    print("node", "A", " B")
    cost, dstPath = A_star(graph, h, eval('A'), eval('B'))
    print('cost:', cost)
    for i in dstPath:
        print(i, end='')
        if i != dstPath[-1]:
            print(" -> ", end='')
    print()

    print("node", "C", " B")
    cost, dstPath = A_star(graph, h, eval('C'), eval('B'))
    print('cost:', cost)
    for i in dstPath:
        print(i, end='')
        if i != dstPath[-1]:
            print(" -> ", end='')
    print()

    print("node", "U", " B")
    cost, dstPath = A_star(graph, h,eval('U'),eval('B'))
    print('cost:', cost)
    for i in dstPath:
        print(i, end='')
        if i != dstPath[-1]:
            print(" -> ", end='')
    print()



