import itertools

input()
data = list(map(int, input().split()))
# print(f'data : {data}')

# poke list
# init 0
poke_list = list(itertools.repeat(0, len(data)))
# print(f'poke_list : {poke_list}')


def back_fill_poke_list(arr, i=1):
    if len(arr) == 0:
        return
    else:
        # compare through all-1 arr item
        for j in range(len(arr)-1):
            if arr[-1] > arr[j]:
                # add to poke list, after compare
                if poke_list[-i] >= poke_list[j]:
                    poke_list[j] = poke_list[-i] + 1
        # print(f'  i : {i}')
        # print(f'  arr :       {arr}')
        # print(f'  poke_list : {poke_list}')

        # recurse
        i += 1
        back_fill_poke_list(arr[:-1], i)


back_fill_poke_list(data)
print(max(poke_list)+1)



