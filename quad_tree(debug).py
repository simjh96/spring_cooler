# 8
# 11110000
# 11110000
# 00011100
# 00011100
# 11110000
# 11110000
# 11110011
# 11110011
import numpy as np

_ = int(input())
seq = []
for i in range(_):
    seq.append([int(j) for j in input()])
seq = np.array(seq)


def quad_tree(sub_seq: '2darray'):
    if len(sub_seq) == 1:
        return int(sub_seq[0][0])
    else:
        n = len(sub_seq)
        quad_tree_ = '(' + str(quad_tree(sub_seq[:n//2, :n//2])) + \
                     str(quad_tree(sub_seq[:n//2, n//2:])) + \
                     str(quad_tree(sub_seq[n//2:, :n//2])) + \
                     str(quad_tree(sub_seq[n//2:, n//2:])) + ')'
        print(' '*(8-len(sub_seq)) + f'sub_seq : {sub_seq}')
        print(' '*(8-len(sub_seq)) + f'quad_tree before pruning : {quad_tree_}')

        quad_tree_ = quad_tree_.replace('(0000)', '0')
        quad_tree_ = quad_tree_.replace('(1111)', '1')
        print(' '*(8-len(sub_seq)) + f'quad_tree after pruning : {quad_tree_}')
        return quad_tree_


print(quad_tree(seq)=='((110(0101))(0010)1(0001))')


