import math


# helper
def multi_slice_append(appended: list, appending: list, row_i: 'from', row_j: 'up to', col_i, col_j) -> 'void':
    for _ in range(row_j - row_i + 1):
        for _1 in range(col_j - col_i + 1):
            appended[row_i + _][col_i + _1] = appending[_][_1]
    return


def matrix_printer(mat:'2darray') -> 'str':
    # [[print(element, end='') for element in row] + [print('\n', end='')] for row in mat]
    result = ''
    for row in mat:
        for element in row:
            result = result + element
        result = result+'\n'
    return result


def star_staker(n_) -> 'block':
    if n_ == 1:
        return [['*','*','*'],['*',' ','*'],['*','*','*']]
    else:
        block = star_staker(n_ - 1)
        block_size = 3**(n_-1)
        grid = [[' ' for _0 in range(3**n_)] for _1 in range(3**n_)]
        grid_ = [[' ' for _0 in range(3**(n_ - 1))] for _1 in range(3**(n_ - 1))]

        # build all
        for _0 in range(3):
            for _1 in range(3):
                multi_slice_append(grid, block,
                                   _0*block_size, (_0+1)*block_size - 1,
                                   _1*block_size, (_1+1)*block_size - 1)

        # pop middle block
        multi_slice_append(grid, grid_,
                           1 * block_size, 2 * block_size - 1,
                           1 * block_size, 2 * block_size - 1)

        return grid


n = int(round(math.log(int(input()), 3),3))
# print(len(star_staker(5)[0])) # 243
result = matrix_printer(star_staker(n))[:-1]
print(len(result))

# with open('star_printer5.txt','w') as x:
#     x.write(result)


