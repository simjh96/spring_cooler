import sys

sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline().strip())
board = []
complex_counts = []


def delta(i, j, di, dj, counter):
    if ((n > i + di >= 0) and (n > j + dj >= 0)) and (board[i + di][j + dj] == 1):
        counter[0] += 1
        board[i + di][j + dj] = 2
        dfs(i + di, j + dj, counter)


def dfs(i, j, counter):
    if board[i][j] == 1:
        counter[0] += 1
        board[i][j] = 2
    delta(i, j, -1, 0, counter)
    delta(i, j, 1, 0, counter)
    delta(i, j, 0, -1, counter)
    delta(i, j, 0, 1, counter)


for _0 in range(n):
    row = list(map(int, sys.stdin.readline().strip()))
    board.append(row)

for row in range(n):
    for col in range(n):
        if board[row][col] == 1:
            counter = [0]
            dfs(row, col, counter)
            complex_counts.append(counter[0])
print(len(complex_counts))
for _ in sorted(complex_counts):
    print(_)
