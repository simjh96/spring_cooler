import sys
sys.setrecursionlimit(10**7)


class Node:
    def __init__(self, name):
        self.name = name
        self.child = dict()   # {1: [cost, time], ...}


class Graph:
    def __init__(self, n, m):
        self.nodes = {_: Node(_) for _ in range(1, n+1)}
        self.n = n
        self.m = m

    def link(self, info):    # info [start, end, cost, time]
        self.nodes[info[0]].child[info[1]] = [info[2], info[3]]

    def dp(self, progress, memo) -> "min total time":
        node = progress[-1]
        if node == self.n:
            return [0, 0]   # [cost, time]
        else:
            if node in memo:
                return memo[node]
            else:
                _nodes = [_ for _ in self.nodes[node].child.items() if _ not in progress]
                dps = []
                for i, [c, t] in _nodes:
                    _dp = self.dp(progress+[i], memo)
                    if _dp and c + _dp[0] <= self.m:   # when further path with matching condition exists
                        dps.append([c + _dp[0], t + _dp[1]])
                if dps:
                    memo[node] = min(dps, key=lambda x: x[1])
                    return memo[node]
                else:
                    memo[node] = None
                    return memo[node]


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())    # (2 ≤ N ≤ 100),(0 ≤ M ≤ 10,000),(0 ≤ K ≤ 10,000)
    G = Graph(n, m)
    for _ in range(k):
        G.link(list(map(int, input().split())))
    memo = dict()
    answer = G.dp([1], memo)
    if answer:
        print(answer[1])
    else:
        print("Poor KCM")











