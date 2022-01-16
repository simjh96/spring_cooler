n = int(input())
A = list(map(int, input().split()))
a_min, a_max = 1, 100001   # a가 가질수 있는 값보다 하나 더 커야지... 미만 이랬는데
p, q, r, S = map(int, input().split())


def score(a, k):
    if a > k + r:
        return a - p
    elif a < k:
        return a + q
    else:
        return a


def find_k():
    l = a_min
    r = a_max
    while l <= r:
        mid = (l+r)//2
        if sum(map(lambda a: score(a, mid), A)) >= S:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans


if sum(map(lambda a: score(a, a_max), A)) < S:
    print(-1)
else:
    answer = find_k()
    print(answer)



