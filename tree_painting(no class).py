# 16% 는 넘는데 0 같은거 처음에 다 걸러내느게 좋을듯

import sys
sys.setrecursionlimit(4*10**5)


class Tree:
    def __init__(self, n):
        self.n = n
        self.root = 0   # always
        self.nodes = {_: [set(), 0] for _ in range(n)}   # i: [adjs, color]

    def link(self, n0: int, n1: int):   # 순방향이 아님
        self.nodes[n0][0].add(n1)
        self.nodes[n1][0].add(n0)

    def color(self, n0, c0):
        self.nodes[n0][1] = c0

    def set_children(self, current=0, parent=-1):
        self.nodes[current][0].discard(parent)
        for _ in self.nodes[current][0]:
            self.set_children(_, current)

    def dp(self, root: int = 0):
        r_color = self.nodes[root][1]
        r_children = self.nodes[root][0]
        if r_children:
            return sum([self.dp(_) if self.nodes[_][1] == r_color else self.dp(_) + 1 for _ in r_children])
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
print(tree.dp() + (1 if tree.nodes[0][1] != 0 else 0))

