import sys
sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, key: 'dual key', state):
        self.key = key
        self.adj = []
        self.state = state


class Graph:
    def __init__(self, _n, _m):
        self.n = _n
        self.m = _m
        self.nodes = [[None for col in range(self.m)]for row in range(self.n)]
        self.super = Node('super', 'super')

    def set_back_links(self):
        for row in range(self.n):
            for col in range(self.m):
                if self.nodes[row][col] is None:
                    pass
                else:
                    if self.nodes[row][col].state == 1:
                        self.super.adj.append((row, col))

                    if row+1<self.n and self.nodes[row+1][col] is not None:
                        self.nodes[row][col].adj.append((row+1, col))
                    if row-1>=0 and self.nodes[row-1][col] is not None:
                        self.nodes[row][col].adj.append((row-1, col))
                    if col+1<self.m and self.nodes[row][col+1] is not None:
                        self.nodes[row][col].adj.append((row, col+1))
                    if col-1>=0 and self.nodes[row][col-1] is not None:
                        self.nodes[row][col].adj.append((row, col-1))

    def input_links(self):
        for row in range(self.n):
            states = list(map(int, input().split()))
            for col in range(self.m):
                if states[col] == -1:
                    pass
                else:
                    self.nodes[row][col] = Node((row, col), states[col])


m, n = map(int, input().split())
G = Graph(n, m)
G.input_links()
G.set_back_links()
visited = set()


# initial front_line == set(super.adj)
def bfs(front_line: set, i=0) -> 'counts':
    if len(front_line)==0:
        return i-1
    else:
        front_line_ = set()
        for node_r, node_c in front_line:
            # if (node_r, node_c) not in visited:
            visited.add((node_r, node_c))
            for r, c in G.nodes[node_r][node_c].adj:
                if (r, c) not in visited:
                    front_line_.add((r, c))
        return bfs(front_line_, i+1)


full = sum(map(lambda x: sum(map(lambda y: y is not None, x)), G.nodes))
i = bfs(set(G.super.adj))
if len(visited)<full:
    print(-1)
else:
    print(i)






