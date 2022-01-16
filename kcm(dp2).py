import sys
sys.setrecursionlimit(10**7)


class Node:
    def __init__(self, name):
        self.child = []   # {1: [cost, time], ...}


class Graph:
    def __init__(self, n, m):
        self.nodes = {_: Node(_) for _ in range(1, n+1)}
        self.n = n
        self.m = m

    def link(self, info):    # info [start, end, cost, time]
        self.nodes[info[0]].child.append([info[1], info[2], info[3]])

    def dp(self, progress, memo, debug=1) -> "min total time":
        print("========================")
        print(debug * ' ' + f'progress: {progress}')
        debug += 1
        node = progress[-1]
        if node in memo:
            print(debug*' ' + f'progress: {progress} -> return: {memo[node]}')
            return memo[node]
        else:
            _nodes = [[_[0], [_[1], _[2]]] for _ in self.nodes[node].child if _[0] not in progress]
            print(debug * ' ' + f'_nodes : {_nodes}')
            dps = []
            for i, [c, t] in _nodes:
                _dp = self.dp(progress + [i], memo, debug)
                print(debug * ' ' + f'_dp: {_dp} and c + _dp[0]: {c + _dp[0]} <= self.m: {self.m}')
                if _dp and c + _dp[0] <= self.m:   # when further path with matching condition exists
                    dps.append([c + _dp[0], t + _dp[1]])
            if dps:
                memo[node] = min(dps, key=lambda x: x[1])
                print(debug*' ' + f'dps: {dps}')
                print(debug*' ' + f'progress: {progress} -> return: {memo[node]}')
                return memo[node]
            else:
                memo[node] = None
                print(debug*' ' + f'progress: {progress} -> return: {memo[node]}')
                return memo[node]


t = int(input())
for _0 in range(t):
    n, m, k = map(int, input().split())    # (2 ≤ N ≤ 100),(0 ≤ M ≤ 10,000),(0 ≤ K ≤ 10,000)
    G = Graph(n, m)
    for _1 in range(k):
        G.link(list(map(int, input().split())))
    memo = {n: [0, 0]}
    answer = G.dp([1], memo)
    if answer is None:
        print("Poor KCM")
    else:
        print(answer[1])











