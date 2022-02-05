import sys
from itertools import accumulate
from bisect import bisect


# set all input
n_s = int(sys.stdin.readline())
c_giris = []   # [[[c_r_n0, c_r_n1, ...], [c_l_n0, ...]], [], []]
for _ in range(n_s):
    inp = sys.stdin.readline()

    giri = enumerate(map(int, inp.split()))
    r_giri = map(lambda x: x[1], filter(lambda x: not x[0] % 2, giri))
    c_r_giri = accumulate(r_giri)

    giri = enumerate(map(int, inp.split()))
    l_giri = map(lambda x: x[1], filter(lambda x: x[0] % 2, giri))
    c_l_giri = accumulate(l_giri)

    c_giris.append([list(c_r_giri), list(c_l_giri)])

# set init
tgt_idx = 0

for i in range(n_s):
    if tgt_idx < 13:   # left deck
        c_i = bisect(c_giris[i][1], tgt_idx)
        tgt_idx += c_giris[i][0][c_i]

    else:   # right deck
        c_i = bisect(c_giris[i][0], tgt_idx - 13)
        if c_i:
            tgt_idx += c_giris[i][1][c_i - 1] - 13
        else:
            tgt_idx += -13
print(tgt_idx + 1)
