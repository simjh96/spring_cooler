import sys

sys.setrecursionlimit(10 ** 9)


class Node:
    def __init__(self, status):
        # path, block, hole
        self.status = status

        self.u = None
        self.d = None
        self.l = None
        self.r = None


class Graph:
    def __init__(self, board):
        self.board = board
        self.r = None
        self.b = None
        # set nodes
        self.nodes = dict()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '#':
                    self.nodes[(r, c)] = Node('b')
                if board[r][c] == '.':
                    self.nodes[(r, c)] = Node('p')
                if board[r][c] == 'R':
                    self.nodes[(r, c)] = Node('p')
                    self.r = (r, c)
                if board[r][c] == 'B':
                    self.nodes[(r, c)] = Node('p')
                    self.b = (r, c)
                if board[r][c] == 'O':
                    self.nodes[(r, c)] = Node('h')

    def set_end(self):
        # embed all nodes
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.nodes.get((r, c)).status == 'p':
                    self.dfs((r, c), 'u')
                    self.dfs((r, c), 'd')
                    self.dfs((r, c), 'l')
                    self.dfs((r, c), 'r')

    def dfs(self, start: tuple, direc: str) -> '(cord, dist) or h':
        r, c = start
        print('====================')
        print(f'start:{start}, direc:{direc}')
        if direc == 'u' and self.nodes.get((r, c)).u is None:
            r_, c_ = r - 1, c
            if self.nodes.get((r_, c_)).status == 'b':
                self.nodes[(r, c)].u = ((r, c), 0)
                print(f'self.nodes[(r, c)].u = ((r, c), 0)')
                return self.nodes[(r, c)].u[0], self.nodes[(r, c)].u[1] + 1
            elif self.nodes.get((r_, c_)).status == 'h':
                self.nodes[(r, c)].u = 'h'
                print(f"self.nodes[(r, c)].u = 'h'")
                return 'h'
            else:
                self.nodes[(r, c)].u = self.dfs((r_, c_), direc)
                print(f"self.nodes[(r, c)].u = self.dfs((r_, c_), direc)")
                return self.nodes[(r, c)].u[0], self.nodes[(r, c)].u[1] + 1
        if direc == 'd' and self.nodes.get((r, c)).d is None:
            r_, c_ = r + 1, c
            if self.nodes.get((r_, c_)).status == 'b':
                self.nodes[(r, c)].d = ((r, c), 0)
                print(f"self.nodes[(r, c)].d = ((r, c), 0)")
                return self.nodes[(r, c)].d[0], self.nodes[(r, c)].d[1] + 1
            elif self.nodes.get((r_, c_)).status == 'h':
                self.nodes[(r, c)].d = 'h'
                print(f"self.nodes[(r, c)].d = 'h'")
                return 'h'
            else:
                self.nodes[(r, c)].d = self.dfs((r_, c_), direc)
                print(f"self.nodes[(r, c)].d = self.dfs((r_, c_), direc)")
                return self.nodes[(r, c)].d[0], self.nodes[(r, c)].d[1] + 1
        if direc == 'l' and self.nodes.get((r, c)).l is None:
            r_, c_ = r, c - 1
            if self.nodes.get((r_, c_)).status == 'b':
                self.nodes[(r, c)].l = ((r, c), 0)
                print(f"self.nodes[(r, c)].l = ((r, c), 0)")
                return self.nodes[(r, c)].l[0], self.nodes[(r, c)].l[1] + 1
            elif self.nodes.get((r_, c_)).status == 'h':
                self.nodes[(r, c)].l = 'h'
                print(f"self.nodes[(r, c)].l = 'h'")
                return 'h'
            else:
                self.nodes[(r, c)].l = self.dfs((r_, c_), direc)
                print(f"self.nodes[(r, c)].l = self.dfs((r_, c_), direc)")
                return self.nodes[(r, c)].l[0], self.nodes[(r, c)].l[1] + 1
        if direc == 'r' and self.nodes.get((r, c)).r is None:
            r_, c_ = r, c + 1
            if self.nodes.get((r_, c_)).status == 'b':
                self.nodes[(r, c)].r = ((r, c), 0)
                print(f"self.nodes[(r, c)].r = ((r, c), 0)")
                return self.nodes[(r, c)].r[0], self.nodes[(r, c)].r[1] + 1
            elif self.nodes.get((r_, c_)).status == 'h':
                self.nodes[(r, c)].r = 'h'
                print(f"self.nodes[(r, c)].r = 'h'")
                return 'h'
            else:
                self.nodes[(r, c)].r = self.dfs((r_, c_), direc)
                print(f"self.nodes[(r, c)].r = self.dfs((r_, c_), direc)")
                return self.nodes[(r, c)].r[0], self.nodes[(r, c)].r[1] + 1


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

print(board)
G = Graph(board)
G.set_end()

print(G.nodes[(1, 1)].d)
