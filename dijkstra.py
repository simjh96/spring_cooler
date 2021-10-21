import heapq
import sys

V, E = map(int, sys.stdin.readline().strip().split())
S = int(sys.stdin.readline().strip())


class Node:
    def __init__(self, key):
        self.key = key
        self.adj = dict()


class Graph:
    def __init__(self, v):
        self.nodes = dict((_, Node(_)) for _ in range(1, v+1))

    def set_link(self, _from: int, _to: int, w: int):
        self.nodes[_from].adj[_to] = w


G = Graph(V)
for _ in range(E):
    G.set_link(*map(int, sys.stdin.readline().strip().split()))

inf = 10**7
distances = dict((_, inf) for _ in range(1, V+1))
distances[S] = 0
result = []

while distances:
    min_node_idx, min_dist = min(distances.items(), key=lambda x: x[1])
    distances.pop(min_node_idx)
    result.append((min_node_idx, min_dist))

    remaining = distances.keys()
    for _to, w in G.nodes[min_node_idx].adj.items():
        if _to in remaining:
            if min_dist + w < distances[_to]:
                distances[_to] = min_dist + w

for _, d in sorted(result):
    if d < 10**7:
        print(d)
    else:
        print('INF')








