# 78% 메모리 초과
# link shrink algo 사용 고려

import sys
sys.setrecursionlimit(70000)


class Node:
    def __init__(self, name):
        self.parent = name


class Graph:
    def __init__(self, n):   # n: number of nodes
        self.nodes = [Node(_) for _ in range(n)]

    def update(self, n0: int, n1: int) -> bool:
        # link n0 and n1 -> cycle formed
        r0, r1 = self.find_root(n0), self.find_root(n1)
        if r0 == r1:
            return True
        else:
            self.nodes[r1].parent = r0
            return False

    def find_root(self, n: int) -> int:
        p = self.nodes[n].parent
        if n == p:
            return n
        else:
            return self.find_root(p)


n, m = map(int, sys.stdin.readline().strip().split())
G = Graph(n)
for _ in range(m):
    if G.update(*map(int, sys.stdin.readline().strip().split())):
        print(_+1)
        break
else:
    print(0)

