# tree is where everything is connected with unique path
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 6)

V = int(sys.stdin.readline().strip())
dists = []
graph = dict()

for _ in range(V):
    _input = list(map(int, sys.stdin.readline().strip().split()))
    graph[_input[0]] = []
    for _0 in range(len(_input[1:-1])//2):
        # {1 : [[3, 2]]}
        graph[_input[0]].append(_input[1+2*_0:1+2*(_0+1)])

# select starting node
for _ in graph:
    if len(graph[_]) == 1:
        start_key = _
        break


def diameter(current_node, in_path=None, _graph=graph, _dists=dists, debug=0) -> 'max among outs':
    debug += 1
    print('  '*debug+f'diameter(current_node : {current_node}, in_path : {in_path})')
    print('  '*debug+f'_graph : {_graph}')
    print('  '*debug+f'_dists : {_dists}')

    if len(_graph[current_node]) == 1 and in_path is not None:
        print('  ' * debug + f'len(_graph[current_node]) == 1 and in_path is not None')
        print('return : 0')
        return 0
    else:
        residual = [[node, dist] for node, dist in _graph[current_node] if node != in_path]

        if len(residual) == 1:
            print('  ' * debug + f'residual == 1')
            next_node, adj_dist = residual[0]
            result = diameter(next_node, current_node, debug=debug) + adj_dist

            print(f'return : {result}')
            return result

        elif len(residual) == 2:
            print('  ' * debug + f'residual == 2')
            child0, child1 = residual
            candidate0 = diameter(child0[0], current_node, debug=debug) + child0[1]
            candidate1 = diameter(child1[0], current_node, debug=debug) + child1[1]

            # append local distance
            _dists.append(candidate0 + candidate1)
            result = max((candidate0, candidate1))

            print(f'return : {result}')
            return result

        # binary 이상의 tree 인것으로 확인 됨
        else:
            candidates = []
            for r in residual:
                candidates.append(diameter(r[0], current_node, debug=debug) + r[1])
            _max = 0
            for c in combinations(candidates, 2):
                if c[0] + c[1] > _max:
                    _max = c[0] + c[1]

            _dists.append(_max)
            return max(candidates)


dists.append(diameter(start_key))
print(max(dists))
print(dists)





