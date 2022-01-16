n, q = map(int, input().split())
p = sorted(list(map(int, input().split())))   # [(0,5), (1,7) ...]
dp = [p[_+1] - p[_] for _ in range(n-1)] + [0]   # d to the right

for _0 in range(q):
    x = int(input())

    # whats left, whats right
    x_l, x_r = n - 1, n   # if not found
    for _1 in range(n):
        if p[_1] >= x:
            x_r = _1   # 0 ~ n+1
            x_l = _1 - 1   # -1 ~ n
            break
    print(f'p[:x_l+1] : {p[:x_l+1]}')
    print(f'p[x_r:] : {p[x_r:]}')


    # all sum of left
    l_score = 0
    if x_l != -1:
        for _0 in range(x_l):
            print("======================")
            print(f'l_score : {l_score}')
            print(f'dp[_0] : {dp[_0]}')
            l_score += dp[_0]*(_0+1)
        print("======================")
        print(f'l_score : {l_score}')
        print(f'dp[_0] : {dp[_0]}')
        l_score += (x - p[x_l])*(x_l+1)


    # all sum of right
    r_score = 0
    if x_r != n:
        print("======================")
        print(f'l_score : {l_score}')
        print(f'dp[_0] : {dp[_0]}')
        r_score += (p[x_r] - x) * (n - x_r)
        for _0 in range(x_r + 1, n):
            print("======================")
            print(f'l_score : {l_score}')
            print(f'dp[_0] : {dp[_0]}')
            r_score += dp[_0 - 1] * (n - _0)

    print(l_score + r_score)



