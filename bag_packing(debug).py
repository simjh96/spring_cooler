def pick_pack(pack: 'idxs' = [], pick: 'idx' = 0, pack_w=0) -> 'void':
    # if (pick == len(weights)) and (pack == []):
    #     print(f'recurse ended')
    #     print(f'  pack : {pack}')
    #     return

    # if pick == len(weights)
    # pack.pop(-1) and pick = next
    if pick == len(weights):
        if pack == []:
            return
        else:
            pick = pack.pop(-1)
            pack_w -= weights[pick]
            print(f'    pick reached end')
            print(f'    pick : {pick}')
            print(f'    pack : {pack}')
    else:
        # pack pick
        pack.append(pick)
        # weight
        pack_w += weights[pick]
        print(f'  pick : {pick}')
        print(f'  pack : {pack}')
        if pack_w >= break_point:
            # record -> pop and recurse
            record.append(sum(values[i] for i in pack))
            debug_pack.append(pack.copy())
            debug_w.append(pack_w)

            pick = pack.pop(-1)
            pack_w -= weights[pick]
            print(f'    break point reached')
            print(f'    pick : {pick}')
            print(f'    pack : {pack}')
    # recurse
    pick += 1
    pick_pack(pack, pick, pack_w)


len_n, K = list(map(int, input().split()))
weights = []
values = []

for i in range(len_n):
    w, v = list(map(int, input().split()))
    weights.append(w)
    values.append(v)

break_point = sum(weights) - K

# if break_point < 0 -> return sum(v)
if break_point <= 0:
    print(sum(values))

else:
    # picking
    # stacking
    # if broken limit -> record/ go back and pick next
    record = []
    debug_pack = []
    debug_w = []

    pick_pack()

    print(f'K : {K}')
    print(f'break_point :  {break_point}')
    print(f'record : {record}')
    print(f'debug_pack : {debug_pack}')
    print(f'debug_w : {debug_w}')
    print(f'weights : {weights}')
    print(f'values : {values}')

    if len(record) == 0:
        print(sum(values))
    else:
        # total value - max(record)
        print(sum(values) - min(record))

