def function_(orders: str, arg_array: list):
    details = list(map(len, orders.split('R')))
    left_cut = 0
    right_cut = 0
    direction = len(details)
    for i in range(len(details)):
        if i % 2:
            right_cut += details[i]
        else:
            left_cut += details[i]

    if len(arg_array) < left_cut+right_cut:
        print('error')
    else:
        if right_cut == 0:
            result = str(arg_array[left_cut:][::(-1) ** (direction + 1)]).replace(' ', '')
            print(result)
        else:
            result = str(arg_array[left_cut:-right_cut][::(-1) ** (direction + 1)]).replace(' ', '')
            print(result)


p = int(sys.stdin.readline().strip())
for p_ in range(p):
    func_array = input()
    _ = input()
    target = input()[1:-1].split(',')
    if target[0] == '':
        target = []
    else:
        target = list(map(int, target))

    # operation
    function_(func_array, target)

