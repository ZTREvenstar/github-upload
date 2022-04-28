import sys
import template.graphAdjacencyList as GraphModule


# src: the id of src node
# 变量类型全部当做Vertex obj处理
# 如需要打印path，则多一个parent list或者给vertex加parent属性
def dijkstra(graph, src):
    if graph is None:
        return None
    src = graph.getVertex(src)
    nodes = [i for i in graph]
    if src not in nodes:
        print("ERROR: src not in nodes.")
        return None

    MAX = sys.maxsize
    distance = {}   # initialize the distance list
    for node in nodes:
        distance[node] = MAX
    distance[src] = 0
    min_node = src  # the node nearest to src
    visited = []

    while len(nodes) != 0:
        visited.append(min_node)
        nodes.remove(min_node)
        for n in min_node.getNeighbors():
            edgeWeight = min_node.getWeight(n)
            if n not in visited and edgeWeight > 0:
                distance[n] = min(distance[n], distance[min_node] + edgeWeight)

        min_dist = MAX  # update the min_node
        for i in distance.keys():
            d = distance[i]
            if i not in visited and 0 < d < min_dist:
                min_dist = d
                min_node = i

    print(distance)
    result = {i.getId(): distance[i] for i in distance}
    return result


if __name__ == "__main__":
    g = GraphModule.Graph()
    for N in range(6):
        g.addVertex(N)

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

    print(dijkstra(g, 0))
