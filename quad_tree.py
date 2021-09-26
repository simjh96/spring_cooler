import sys
sys.setrecursionlimit(10**6)

_ = int(input())
seq = []
for i in range(_):
    seq.append([int(j) for j in input()])


def quad_tree(sub_seq: '2darray'):
    if len(sub_seq) == 1:
        return int(sub_seq[0][0])
    else:
        n = len(sub_seq)
        quad_tree_ = '(' + str(quad_tree(sub_seq[:n//2, :n//2])) + \
                     str(quad_tree(sub_seq[:n//2, n//2:])) + \
                     str(quad_tree(sub_seq[n//2:, :n//2])) + \
                     str(quad_tree(sub_seq[n//2:, n//2:])) + ')'
        quad_tree_ = quad_tree_.replace('(0000)', '0')
        quad_tree_ = quad_tree_.replace('(1111)', '1')
        return quad_tree_


print(quad_tree(seq))


