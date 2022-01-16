import math


def mod_change(_n, _d) -> list:
    rev_base = ''

    while _n > 0:
        _n, mod = divmod(_n, _d)
        rev_base += str(mod)

    return int(rev_base[::-1])


def decoder(n):
    results = []   # [d-1개 중 몇번째 사용했는지, d-2개 중 몇번째 사용했는지 ...]
    samples = [_ for _ in range(d)]
    for _ in sorted(list(range(d)), reverse=True):
        r = n // math.factorial(_)
        n = n - math.factorial(_)*r
        results.append(str(samples[r]))
        samples.pop(r)

    return int(''.join(results))


n, d = map(int, input().split())
n = n + 1
m_n = mod_change(n, d)


def solution():
    # find least greater or equal
    left = 0
    right = math.factorial(d) - 1
    # ones bigger needs to be cut
    if m_n > decoder(right):
        return -1

    while left <= right:
        mid = (left+right)//2
        if decoder(mid) >= m_n:
            nearest = mid
            right = mid - 1
        else:
            left = mid + 1

    # ones starting with 0 needs to be increased to 102345..
    min_m_n = [str(_) for _ in sorted(list(range(d)))]
    min_m_n[0] = '1'
    min_m_n[1] = '0'

    if decoder(nearest) < int(''.join(min_m_n)):
        # print(f"min_m_n : {min_m_n}, {int(''.join(min_m_n), d)}")
        return int(''.join(min_m_n), d)
    else:
        # print(f"nearest : {decoder(nearest)}, {int(str(decoder(nearest)), d)}")
        return int(str(decoder(nearest)), d)


print(solution())
