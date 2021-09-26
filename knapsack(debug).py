k = 7
wvs = [[6, 13],
       [4, 8],
       [3, 6],
       [5, 12]]


# seq
def knapsack(sub_seq, buffer_weight, memo):
    if (len(sub_seq), buffer_weight) in memo:
        print('  '*(4 - len(sub_seq)) + f'combination of (len(sub_seq):{len(sub_seq)}, buffer_weight:{buffer_weight}) in memo : {memo[(len(sub_seq), buffer_weight)]}')
        return memo[(len(sub_seq), buffer_weight)]
    else:
        if buffer_weight >= sub_seq[0][0]:
            take = knapsack(sub_seq[1:], buffer_weight - sub_seq[0][0], memo) + sub_seq[0][1]
        else:
            take = 0

        leave = knapsack(sub_seq[1:], buffer_weight, memo)
        print('  '*(4 - len(sub_seq)) + f'sub_seq : {sub_seq}')
        print('  '*(4 - len(sub_seq)) + f'buffer_weight : {buffer_weight}')
        print('  '*(4 - len(sub_seq)) + f'sub_seq[0][0] : {sub_seq[0][0]}')
        print('  '*(4 - len(sub_seq)) + f'{[f"too heavy : 0" if take==0 else f"take : {take}" ][0]}')
        print('  '*(4 - len(sub_seq)) + f'leave : {leave}')
        print('  '*(4 - len(sub_seq)) + f'{[f"take" if take > leave else f"leave"]}')
        choice = max(take, leave)
        memo[(len(sub_seq), buffer_weight)] = choice
        print('  ' * (4 - len(
            sub_seq)) + f'memo saved : {memo[(len(sub_seq), buffer_weight)]}')
        return choice


# memoaize with base case
memo = dict()
for i in range(k+1):
    memo[(0, i)] = 0
print(knapsack(wvs, k, memo))
