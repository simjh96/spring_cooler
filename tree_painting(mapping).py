import sys
sys.setrecursionlimit(10**5)


class Node:
    def __init__(self):
        self.children = []
        self.adj = []
        self.color = 0


class Tree:
    def __init__(self, n):
        self.n = n
        self.root = 0   # always
        self.nodes = {_: Node() for _ in range(n)}
        self.visited = set()

    def link(self, n0: int, n1: int):   # 순방향이 아님
        self.nodes[n0].adj.append(n1)
        self.nodes[n1].adj.append(n0)

    def color(self, n0, c0):
        self.nodes[n0].color = c0

    def set_children(self, current=0, parent=-1):
        for _ in self.nodes[current].adj:
            if _ != parent:
                self.nodes[current].children.append(_)
                self.set_children(_, current)

    def dp(self, root: int = 0):
        r_color = self.nodes[root].color
        r_children = self.nodes[root].children
        if r_children:
            return sum([self.dp(_) if self.nodes[_].color == r_color else self.dp(_) + 1 for _ in r_children])
        else:
            return 0


n = int(sys.stdin.readline().strip())
tree = Tree(n)
tgt = list(map(int, sys.stdin.readline().strip().split()))
for _ in range(len(tgt)):
    tree.color(_, tgt[_])

for _ in range(n-1):
    p, c = map(int, sys.stdin.readline().strip().split())
    tree.link(p-1, c-1)
tree.set_children()
print(tree.dp())

