import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.adj = []
        self.color = 0


class Tree:
    def __init__(self, n):
        self.root = 0   # always
        self.nodes = {_: Node(_) for _ in range(n)}
        self.size = -1   # nodes with color 0 is all truncated except 0

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

    def bfs(self, current: int):
        cs = self.nodes[current].children
        i = 0
        needless = set()
        while i < len(cs):
            # print(f'i: {i}')
            # print(f'cs: {cs}')
            if self.nodes[cs[i]].color == self.nodes[current].color:   # paint can be skipped
                needless.add(cs[i])
                cs.extend(self.nodes[cs[i]].children)
            i += 1
        self.nodes[current].children = list(set(cs) - needless)   # final truncated
        # print(f'final cs: {self.nodes[current].children}')

        # next
        for child in self.nodes[current].children:   # recurse for all independent children
            self.bfs(child)

    def count(self, root):
        self.size += 1
        for _ in self.nodes[root].children:
            self.count(_)


n = int(sys.stdin.readline().strip())
tree = Tree(n)
tgt = list(map(int, sys.stdin.readline().strip().split()))
for _ in range(len(tgt)):
    tree.color(_, tgt[_])

for _ in range(n-1):
    p, c = map(int, sys.stdin.readline().strip().split())
    tree.link(p-1, c-1)
tree.set_children()
tree.bfs(tree.root)
tree.count(tree.root)
print(tree.size)
