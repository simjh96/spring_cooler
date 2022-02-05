import sys
sys.setrecursionlimit(10**5)


n = int(sys.stdin.readline().strip())
panels = []
for _ in range(n):
    panels.append(list(map(int, sys.stdin.readline().strip().split())))
panels.sort(key=lambda x: x[0])


def check(p0, p1):
    # reachable and extending
    if 2 * p0[1] - p0[0] >= p1[0]:
        return True
    else:
        return False


def s(ps: list, idx: int = 0, memo: dict = {}) -> int:
    # return max reach

    if idx in memo:   # use memo
        return memo[idx]

    i = 0
    nexts = []  # [idx+1, ...]
    while idx + i < len(ps) - 1:   # build nexts
        i += 1
        if check(ps[idx], ps[idx + i]):
            if ps[idx + i - 1][1] < ps[idx + i][1]:
                nexts.append(idx + i)
        else:
            break

    if nexts:
        memo[idx] = max([s(ps, _, memo) for _ in nexts])
        return memo[idx]
    else:
        return ps[idx][1]


print(s(panels))
