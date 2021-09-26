
# 8
# 11110000
# 11110000
# 00011100
# 00011100
# 11110000
# 11110000
# 11110011
# 11110011

_ = int(input())
seq = []
for i in range(_):
    seq.append([int(j) for j in input()])


def quards(sub_seq: '2darray'):
    n = len(sub_seq)
    top0 = [i0[:n//2] for i0 in sub_seq[:n//2]]
    top1 = [i0[n//2:] for i0 in sub_seq[:n//2]]
    bottom0 = [i0[:n//2] for i0 in sub_seq[n//2:]]
    bottom1 = [i0[n//2:] for i0 in sub_seq[n//2:]]
    return [top0, top1, bottom0, bottom1]


def quad_tree(sub_seq: '2dlist'):
    if len(sub_seq) == 1:
        return int(sub_seq[0][0])
    else:
        n = len(sub_seq)
        t0, t1, b0, b1 = quards(sub_seq)
        quad_tree_ = '(' + str(quad_tree(t0)) + \
                     str(quad_tree(t1)) + \
                     str(quad_tree(b0)) + \
                     str(quad_tree(b1)) + ')'
        print(' '*(8-len(sub_seq)) + f'sub_seq : {sub_seq}')
        print(' '*(8-len(sub_seq)) + f'quad_tree before pruning : {quad_tree_}')

        quad_tree_ = quad_tree_.replace('(0000)', '0')
        quad_tree_ = quad_tree_.replace('(1111)', '1')
        print(' '*(8-len(sub_seq)) + f'quad_tree after pruning : {quad_tree_}')
        return quad_tree_

print(quad_tree(seq)=='((110(0101))(0010)1(0001))')
