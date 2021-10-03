import sys
len_n = int(sys.stdin.readline().strip())
list_a = list(map(int, sys.stdin.readline().strip().split()))

list_a_reversed = list_a[::-1]
reversed_nge = list()
reversed_nge_org = list()
max_num = [-1]


def nge(i, reversed_list, record, comparison_pool, great_wall: object):
    # going to stack in opposite order
    # look up i
    # compare with i - 1
    r_l_i = reversed_list[i]

    # if biggest -1 and reset comparison pool with num
    if r_l_i >= great_wall[0]:
        record.append(-1)
        comparison_pool[:] = []
        print('  '*i + f'r_l[i] : {r_l_i} >= great_wall[0] : {great_wall[0]}')
        print('  '*i + f'i : {i}')
        print('  '*i + f'record : {record}')
        print('  ' * i + f'comparison_pool : {comparison_pool}')
        great_wall[0] = r_l_i

    # comparison_pool의 new element는 이걸로만 채워짐, 나머지는 다시 쓰는값
    elif r_l_i < reversed_list[i - 1]:
        record.append(reversed_list[i - 1])
        # if comparison_pool[-1] != reversed_list[i - 1]:
        comparison_pool.append(reversed_list[i - 1])
        print('  '*i + f'r_l[i] : {r_l_i} < r_l[i-1] : {reversed_list[i - 1]}')
        print('  '*i + f'i : {i}')
        print('  '*i + f'record : {record}')
        print('  ' * i + f'comparison_pool : {comparison_pool}')

    # compare with current comparison_pool
    # binary search
    else:
        flag = 0
        left = 0
        right = len(comparison_pool) - 1
        sorted_comp = sorted(comparison_pool, reverse=True)
        # if flag = 0, end with left == right
        while left < right:
            mid = left + (right - left)//2
            print('  ' * i + f' ==============       binary search begin         ==============')
            print('  ' * i + f' ==============comparison_pool : {comparison_pool}==============')
            print('  ' * i + f' mid : {mid}')

            if r_l_i == comparison_pool[mid]:
                # next is nge
                _ = mid - 1
                record.append(comparison_pool[mid - 1])
                flag = 1
                print('  ' * i + f' found r_l_i == comparison_pool[{mid}] : {comparison_pool[mid]}')
                print('  ' * i + f' append : {comparison_pool[mid - 1]}')
                break
            elif r_l_i > comparison_pool[mid]:
                print('  ' * i + f' r_l_i : {r_l_i} > comparison_pool[mid] : {comparison_pool[mid]}')
                print('  ' * i + f' contracting right edge : {comparison_pool[right]} -> {comparison_pool[mid - 1]}')
                right = mid - 1

            else:
                print('  ' * i + f' r_l_i : {r_l_i} < comparison_pool[mid] : {comparison_pool[mid]}')
                print('  ' * i + f' contracting left edge : {comparison_pool[left]} -> {comparison_pool[mid + 1]}')
                left = mid + 1

        if flag == 0:
            if r_l_i < comparison_pool[left]:
                _ = comparison_pool[left]
                record.append(comparison_pool[left])
                print('  ' * i + f' for r_l_i : {r_l_i} append {comparison_pool[left]} among {comparison_pool}')
            else:
                _ = comparison_pool[left - 1]
                record.append(comparison_pool[left - 1])
                print('  ' * i + f' for r_l_i : {r_l_i} append {comparison_pool[left - 1]} among {comparison_pool}')

        print('  ' * i + f' ==============        binary search end          ==============')
        print('  ' * i + f'r_l[i] : {r_l_i} < _ : {_}')
        print('  ' * i + f'i : {i}')
        print('  ' * i + f'record : {record}')


for _ in range(len_n):
    nge(_, list_a_reversed, reversed_nge, reversed_nge_org, max_num)

print(reversed_nge[::-1])
