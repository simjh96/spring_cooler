n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(board)

memo = dict()


def dp(i, j):
    if i == 0:
        return 1
    else:
        if (i, j) in memo:
            return memo[(i, j)]
        else:
            result = 0
            if j-1 >= 0 and board[i-1][j-1]:
                result += dp(i-1, j-1)
            if board[i-1][j]:
                result += dp(i-1, j)
            if j+1 < m and board[i-1][j+1]:
                result += dp(i-1, j+1)
            memo[(i, j)] = result
            return memo[(i, j)]


result = 0
for _ in range(m):
    if board[n-1][_]:
        result += dp(n-1, _)

print(result)
