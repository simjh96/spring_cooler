# 색종이
import sys
sys.setrecursionlimit(10 ** 6)


# debug
def multi_slice_append(appended: list, appending: list, row_i: 'from', row_j: 'up to', col_i, col_j) -> 'void':
    for _ in range(row_j - row_i + 1):
        for _1 in range(col_j - col_i + 1):
            appended[row_i + _][col_i + _1] = appending[_][_1]
    return

# function
def quad(arr: '1/4', row_i, row_j, col_i, col_j, white_blues: list, debug=0) -> 'homo/hetro':
    debug_grid = [[8 for _ in range(8)] for _1 in range(8)]
    if row_i == row_j:
        return arr[row_i][col_i]

    else:
        # get topo higher statistics
        arr_len = row_j - row_i + 1
        top_left = quad(arr,
                        row_i, row_j - arr_len // 2,
                        col_i, col_j - arr_len // 2,
                        white_blues, debug + 1)
        multi_slice_append(debug_grid, [[top_left for _ in range(arr_len//2)] for _1 in range(arr_len//2)],
                           row_i, row_j - arr_len // 2,
                           col_i, col_j - arr_len // 2)
        top_right = quad(arr,
                         row_i, row_j - arr_len // 2,
                         col_j - arr_len // 2 + 1, col_j,
                         white_blues, debug + 1)
        multi_slice_append(debug_grid, [[top_right for _ in range(arr_len//2)] for _1 in range(arr_len//2)],
                           row_i, row_j - arr_len // 2,
                           col_j - arr_len // 2 + 1, col_j)
        bottom_left = quad(arr,
                           row_j - arr_len // 2 + 1, row_j,
                           col_i, col_j - arr_len // 2,
                           white_blues, debug + 1)
        multi_slice_append(debug_grid, [[bottom_left for _ in range(arr_len//2)] for _1 in range(arr_len//2)],
                           row_j - arr_len // 2 + 1, row_j,
                           col_i, col_j - arr_len // 2)
        bottom_right = quad(arr,
                            row_j - arr_len // 2 + 1, row_j,
                            col_j - arr_len // 2 + 1, col_j,
                            white_blues, debug + 1)
        multi_slice_append(debug_grid, [[bottom_right for _ in range(arr_len//2)] for _1 in range(arr_len//2)],
                           row_j - arr_len // 2 + 1, row_j,
                           col_j - arr_len // 2 + 1, col_j)
        print("===================================================================================")
        print(debug,'th')
        [print(row) for row in debug_grid]
        print("===================================================================================")

        result = [top_left, top_right, bottom_left, bottom_right]

        # homo
        if all([r == 1 for r in result]):
            print('  ' * debug + f'1 s')
            print('  ' * debug + f'result : {result[0:2]}')
            print('  ' * debug + f'         {result[2:4]}')
            print('  ' * debug + f'white_blues : {white_blues}')
            return 1
        elif not any(result):
            print('  ' * debug + f'0 s')
            print('  ' * debug + f'result : {result[0:2]}')
            print('  ' * debug + f'         {result[2:4]}')
            print('  ' * debug + f'white_blues : {white_blues}')
            return 0

        # after clearing
        elif any([r == 2 for r in result]):
            for r in result:
                if r == 1:
                    white_blues[1] += 1
                elif r == 0:
                    white_blues[0] += 1
            print('  ' * debug + f'after clearing')
            print('  ' * debug + f'result : {result[0:2]}')
            print('  ' * debug + f'         {result[2:4]}')
            print('  ' * debug + f'white_blues : {white_blues}')
            return 2

        # first encounter
        else:
            # clearing
            # count after clearing
            # if homo -> 0 or 1(until clearing) / hetero -> 2(keep dividing)
            for r in result:
                if r == 1:
                    white_blues[1] += 1
                elif r == 0:
                    white_blues[0] += 1
            print('  '*debug+f'first encounter')
            print('  '*debug+f'result : {result[0:2]}')
            print('  '*debug+f'         {result[2:4]}')
            print('  '*debug+f'white_blues : {white_blues}')

            return 2


# input
n = int(sys.stdin.readline().strip())

# 2d array로 바꾸기
mat = []
for row in range(n):
    mat.append(list(map(int, sys.stdin.readline().strip().split())))

[print(row) for row in mat]

# counter 1 , 2
wbs = [0, 0]

last = quad(mat, 0, len(mat)-1, 0, len(mat)-1, wbs)

# 0 이나 1 로 종결되는 경우
if not (wbs[0] + wbs[1]):
    if last:
        wbs[1] += 1
    else:
        wbs[0] += 1
print(wbs[0])
print(wbs[1])