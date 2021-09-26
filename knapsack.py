len_n, k = list(map(int, input().split()))
wvs = []
for i in range(len_n):
    w, v = list(map(int, input().split()))
    wvs.append([w, v])


# seq
def knapsack(sub_seq, buffer_weight, memo):
    if (len(sub_seq), buffer_weight) in memo:
        return memo[(len(sub_seq), buffer_weight)]
    else:
        if buffer_weight >= sub_seq[0][0]:
            take = knapsack(sub_seq[1:], buffer_weight - sub_seq[0][0], memo) + sub_seq[0][1]
        else:
            take = 0
        leave = knapsack(sub_seq[1:], buffer_weight, memo)
        choice = max(take, leave)
        memo[(len(sub_seq), buffer_weight)] = choice
        return choice


memo = dict()
for i in range(k+1):
    memo[(0, i)] = 0
print(knapsack(wvs, k, memo))
