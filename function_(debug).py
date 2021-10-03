# ㅋㅋㅋㅋ 출력문 결과가 같아도 출력을 한번에 안하면 오답 처리됨 ..... 결과 저장후 -> 출력 형식으로 해야함

import sys


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

    # print(f'orders:{orders}, arg_array:{arg_array}, details:{details}, left_cut:{left_cut}, right_cut:{right_cut}, direction:{direction},')
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
    # input
    func_array = sys.stdin.readline().strip()
    _ = sys.stdin.readline()
    target = sys.stdin.readline().strip()[1:-1].split(',')
    if target[0] == '':
        target = []
    else:
        target = list(map(int, target))

    # operation
    function_(func_array, target)

