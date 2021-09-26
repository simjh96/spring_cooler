import sys

sys.setrecursionlimit(10 ** 6)


def pick_pack(pack: 'idxs' = [], pick: 'idx' = 0, pack_w=0, record=10**6) -> 'void':
    if pick == len(weights):
        if pack == []:
            return record
        else:
            pick = pack.pop(-1)
            pack_w -= weights[pick]
    else:
        pack.append(pick)
        pack_w += weights[pick]
        if pack_w >= break_point:
            record = min([record, sum(values[i] for i in pack)])
            pick = pack.pop(-1)
            pack_w -= weights[pick]
    pick += 1
    return pick_pack(pack, pick, pack_w, record)


len_n, K = list(map(int, input().split()))
weights = []
values = []
for i in range(len_n):
    w, v = list(map(int, input().split()))
    weights.append(w)
    values.append(v)
break_point = sum(weights) - K

if break_point <= 0:
    print(sum(values))
else:
    record = 10**6
    record = pick_pack(record=record)
    if record == 10**6:
        print(sum(values))
    else:
        print(sum(values) - record)
