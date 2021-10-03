import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
board = []
complex_counts = []
counter = [0]


def delta(i, j, di, dj, counter):
    if ((n > i + di >= 0) and (n > j + dj >= 0)) and (board[i + di][j + dj] == 1):
        counter[0] += 1
        print(f'  delta called : count = {counter[0]}')

        board[i + di][j + dj] = 2
        dfs(i + di, j + dj, counter)

    else:
        print('  delta called : nothing happened')


def dfs(i, j, counter):
    print('====================================================================')
    [print(row) for row in board]
    print('====================================================================')
    # start
    if board[i][j] == 1:
        counter[0] += 1
        board[i][j] = 2

    # up
    # if (i - 1 >= 0) and (board[i - 1][j] == 1):
    #     counter[0] += 1
    #     board[i - 1][j] = 2
    #     dfs(i - 1, j, counter)
    print(f'current position : [{i}],[{j}]')
    print('up')
    delta(i, j, -1, 0, counter)
    print('down')
    delta(i, j, 1, 0, counter)
    print('left')
    delta(i, j, 0, -1, counter)
    print('right')
    delta(i, j, 0, 1, counter)


# original chess board
print('original board')
for _0 in range(n):
    row = list(map(int, sys.stdin.readline().strip()))
    print(row)
    board.append(row)

for row in range(n):
    for col in range(n):
        if board[row][col] == 1:
            dfs(row, col, counter)
            complex_counts.append(counter[0])
            counter = [0]

print(len(complex_counts))
for _ in sorted(complex_counts):
    print(_)

