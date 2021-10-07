def moneys(arr, memo, depth=0) -> 'total money':
    print(' ' * depth + f'call for')
    print(' ' * depth + f'arr:{arr}')
    print(' ' * depth + f'memo:{memo}')

    if memo[len(arr) - 1] is not None:
        print(' ' * depth + f'replaced with memo:{memo}')
        return memo[len(arr) - 1]
    elif len(arr) <= 2:
        print(' ' * depth + f'trivial case : max(arr) : {max(arr)}')
        memo[len(arr) - 1] = max(arr)
        return max(arr)
    else:
        rob = moneys(arr[2:], memo, depth=depth + 1) + arr[0]
        not_rob = moneys(arr[1:], memo, depth=depth + 1)
        choice = max(rob, not_rob)
        print(' ' * depth + f'append memo:{memo}')
        memo[len(arr) - 1] = choice
        print(' ' * depth + f'with :{choice}')
        return choice


def solution(money):
    if len(money) == 3:
        return max(money)
    first = money[0] + moneys(money[2:-1], [None] * len(money[2:-1]))
    second = moneys(money[1:], [None] * len(money[1:]))
    return max(first, second)


money = [3, 5, 6, 3, 6, 7, 3, 4, 6, 7, 8, 9]
solution(money)