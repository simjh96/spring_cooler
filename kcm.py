class Node:
    def __init__(self, name):
        self.name = name
        self.parent = dict()   # {1: [cost, time], ...}
        self.child = dict()   # {1: [cost, time], ...}


class Graph:
    def __init__(self, n, m):
        self.nodes = dict()
        self.end = n
        self.budget = m
        self.answer = "Poor KCM"

    def solvable(self):
        # check solvable
        if self.nodes.get(1) and self.nodes.get(self.end):
            if self.nodes.get(1).child and self.nodes.get(self.end).parent:
                return True
        else:
            return False

    def link(self, info):    # info [start, end, cost, time]
        # init nodes
        if info[0] not in self.nodes:
            self.nodes[info[0]] = Node(info[0])
        if info[1] not in self.nodes:
            self.nodes[info[1]] = Node(info[1])

        # set links
        self.nodes[info[0]].child[info[1]] = [info[2], info[3]]
        self.nodes[info[1]].parent[info[0]] = [info[2], info[3]]

    def dfs(self, progress, total_cost, total_time):
        # use after solvable
        # dist sorting, for reachable nodes
        # dfs in order of most shortest -> most far
        # print("=====================")
        # print(f'progress: {progress}, total_cost: {total_cost}, total_time: {total_time}')
        if self.answer != "Poor KCM":
            return
        if progress[-1] == self.end:
            self.answer = total_time
        else:
            sorted_child = sorted(list(self.nodes[progress[-1]].child.items()), key=lambda x: x[1][1])
            # print(f'progress: {progress}, sorted_child: {sorted_child}, total_time: {total_time}')
            for i, [c, t] in sorted_child:   # child = [i, [cost, time]]
                if i not in progress:   # no going back
                    if total_cost + c <= self.budget:
                        self.dfs(progress+[i], total_cost + c, total_time + t)


t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())    # (2 ≤ N ≤ 100),(0 ≤ M ≤ 10,000),(0 ≤ K ≤ 10,000)
    G = Graph(n, m)
    for _ in range(k):
        G.link(list(map(int, input().split())))
    # print(G.nodes)
    if G.solvable():
        G.dfs([1], 0, 0)
    print(G.answer)








