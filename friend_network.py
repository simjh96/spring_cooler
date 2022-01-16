class Node:
    def __init__(self, name):
        self.name = name
        self.parent = self
        self.len = 1


class Graph:
    def __init__(self):
        self.name2node = dict()  # {"Fred" : Node("Fred")}
        self.visited = set()

    def update(self, f0: str, f1: str, idx=0):
        if f0 not in self.visited:
            self.name2node[f0] = Node(f0)
            self.visited.add(f0)
        if f1 not in self.visited:
            self.name2node[f1] = Node(f1)
            self.visited.add(f1)
        return self.link(f0, f1, idx)

    def link(self, f0: str, f1: str, idx):
        # path compression
        p0, p1 = self.find(self.name2node[f0]), self.find(self.name2node[f1])
        if p0 != p1:
            # merge to f1 -> set len
            p0.parent = p1
            p1.len += p0.len
        return p1.len

    def find(self, n: Node):
        if n.parent != n:
            n.parent = self.find(n.parent)
        return n.parent

    def lookup(self, n: Node, ans):
        if n.parent != n:
            self.lookup(n.parent, ans)
        else:
            ans.append(n)


answer = []
n = int(input())
for _0 in range(n):
    m = int(input())
    G = Graph()
    for _1 in range(m):
        answer.append(str(G.update(*input().split(), idx=_1)))
print('\n'.join(answer))

