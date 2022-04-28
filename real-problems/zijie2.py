myinput = input()
myinput = myinput.split()

'''
4 3
0 1 0 0
1 0 1 1
0 1 0 0
0 1 0 0
0 2 3
'''

# 总人数
N = int(myinput[0])
# 被感染人数
n = int(myinput[1])

Graph = []
for i in range(N):
    temp = input()
    temp = temp.split()
    temparr = []
    for j in range(N):
        temparr.append(int(temp[j]))
    Graph.append(temparr)
# print(Graph)

keypoints = []
myinput = input()
myinput = myinput.split(" ")
for i in myinput:
    keypoints.append(int(i))
# print(keypoints)

keypointNameToIndex = {}
for i in range(n):
    keypointNameToIndex[keypoints[i]] = i
# print(keypointNameToIndex)

# using dijkstra to find distance
Distance = [[-1] * n for _ in range(n)]


def findDistance(src):
    # src: index of a keypoint
    # the list returned stores distance from a to all other keypoints
    if Graph is None:
        return None
    nodes = [i for i in range(n)]
    if src not in nodes:
        print("ERROR: src not in nodes.")
        return None

    MAX = 100000000
    distance = {}  # initialize the distance list
    for node in nodes:
        distance[node] = MAX
    distance[src] = 0
    min_node = src  # the node nearest to src
    visited = []

    while len(nodes) != 0:
        visited.append(min_node)
        nodes.remove(min_node)



