class Node:
    def __init__(self, name):
        self.name = name
        self.child = dict()   # {1: [cost, time], ...}


class Graph:
    def __init__(self, n, m):
        self.nodes = dict()
        self.end = n
        self.budget = m
        self.answer = 10**6

    def link(self, info):    # info [start, end, cost, time]
        # init nodes
        if info[0] not in self.nodes:
            self.nodes[info[0]] = Node(info[0])
        if info[1] not in self.nodes:
            self.nodes[info[1]] = Node(info[1])

        # set links
        self.nodes[info[0]].child[info[1]] = [info[2], info[3]]

    # memo를 넣을 방법을 모르겠네
    def dfs(self, progress, total_cost, total_time):
        if progress[-1] == self.end and total_time < self.answer:
            self.answer = total_time
        else:
            sorted_child = sorted(list(self.nodes[progress[-1]].child.items()), key=lambda x: x[1][1])
            for i, [c, t] in sorted_child:   # child = [i, [cost, time]]
                if i not in progress:   # no going back
                    if total_cost + c <= self.budget:
                        self.dfs(progress+[i], total_cost + c, total_time + t)


t = int(input())

for _0 in range(t):
    n, m, k = map(int, input().split())    # (2 ≤ N ≤ 100),(0 ≤ M ≤ 10,000),(0 ≤ K ≤ 10,000)
    G = Graph(n, m)
    for _1 in range(k):
        G.link(list(map(int, input().split())))
    if G.nodes[1]:
        G.dfs([1], 0, 0)
        if G.answer != 10**6:
            print(G.answer)
        else:
            print("Poor KCM")
    else:
        print("Poor KCM")










