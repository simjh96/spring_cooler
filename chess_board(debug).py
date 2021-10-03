import sys


def abs_subtract(list1, list2):
    n = len(list1)
    m = len(list1[0])
    result = []
    for _ in range(n):
        result.append([abs(list1[_][_1] - list2[_][_1]) for _1 in range(m)])
    return result


def multi_slice_sum(list0, row_i, row_j, col_i, col_j):
    result = 0
    print('    slice to sum')
    if row_i == row_j:
        for _1 in range(col_j - col_i):
            result += list0[row_i][col_i + _1]
    elif col_i == col_j:
        for _ in range(row_j - row_i):
            result += list0[row_i + _][col_i]
    else:
        for _ in range(row_j - row_i + 1):
            debug = []
            for _1 in range(col_j - col_i + 1):
                result += list0[row_i + _][col_i + _1]
                debug.append(list0[row_i + _][col_i + _1])
            print('        ',sep='')
            print(debug)
    return result


def sliding_window(multi_list):
    n = len(multi_list)
    m = len(multi_list[0])
    init_i = [0, 7]
    init_j = [0, 7]
    min_sum = multi_slice_sum(multi_list, init_i[0], init_i[1], init_j[0], init_j[1])

    for _ in range(n - 7):
        for _1 in range(m - 7):
            new_sum = multi_slice_sum(multi_list, init_i[0] + _, init_i[1] + _, init_j[0] + _1, init_j[1] + _1)
            if new_sum < min_sum:
                print(f'  new min_sum : {new_sum}')
                min_sum = new_sum
    return min_sum


n, m = list(map(int, sys.stdin.readline().split()))
board = []

for _0 in range(n):
    row = list(sys.stdin.readline().strip())
    print(row)
    board.append([1 if color=='B' else 0 for color in row])

# original chess board
print('original board')
[print(row) for row in board]

# optimal chess board
# black
black = []
for _1 in range(n):
    if _1 % 2:
        black.append([1 if _2 % 2 else 0 for _2 in range(m)])
    else:
        black.append([0 if _3 % 2 else 1 for _3 in range(m)])
# white
white = []
for _1 in range(n):
    if _1 % 2:
        white.append([0 if _2 % 2 else 1 for _2 in range(m)])
    else:
        white.append([1 if _3 % 2 else 0 for _3 in range(m)])

print('black')
[print(row) for row in black]
print('white')
[print(row) for row in white]

print('==========================abs_subtract==========================')
print('black')
print([print(row) for row in abs_subtract(board, black)])
print('white')
print([print(row) for row in abs_subtract(board, white)])

print('==========================executing operation==========================')
print(sliding_window(abs_subtract(board, black)))
print('==========================executing operation==========================')
print(sliding_window(abs_subtract(board, white)))

