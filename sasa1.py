from collections import defaultdict

n = int(input())
r = {_: list(map(int, input().split())) for _ in range(n+1)}


def power(r_i, s_i):
    return max([0, r[s_i][2] - (abs(r[s_i][0]-r[r_i][0]) + abs(r[s_i][1]-r[r_i][1]))])


all_p = defaultdict(list)
for r_i in range(1, n+1):
    for s_i in range(n+1):
        # including r0
        all_p[r_i].append(power(r_i, s_i))


def actual(r_i):
    return max([all_p[r_i][0] - sum(all_p[r_i][1:]), 0])


answer = max([actual(_) for _ in range(1, n+1)])
if answer:
    print(answer)
else:
    print("IMPOSSIBLE")
