import sys
import heapq

from itertools import combinations

sys.setrecursionlimit(10 ** 6)

V = int(sys.stdin.readline().strip())
dists = []
graph = dict()
for _ in range(V):
    _input = list(map(int, sys.stdin.readline().strip().split()))
    graph[_input[0]] = []
    for _0 in range(len(_input[1:-1])//2):
        graph[_input[0]].append(_input[1+2*_0:1+2*(_0+1)])
for _ in graph:
    if len(graph[_]) == 1:
        start_key = _
        break


def diameter(current_node, in_path=None, _graph=graph, _dists=dists) -> 'max among outs':
    if len(_graph[current_node]) == 1 and in_path is not None:
        return 0
    else:
        residual = [[node, dist] for node, dist in _graph[current_node] if node != in_path]
        if len(residual) == 1:
            next_node, adj_dist = residual[0]
            result = diameter(next_node, current_node) + adj_dist
            return result
        else:
            candidates = []
            for r in residual:
                candidates.append(diameter(r[0], current_node) + r[1])
            first, second = heapq.nlargest(2, candidates)
            _dists.append(first+second)
            return max(candidates)


dists.append(diameter(start_key))
print(max(dists))
