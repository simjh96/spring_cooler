import sys
from bisect import bisect


# set all input
n_s = int(sys.stdin.readline().strip())
c_giris = []   # [[[c_r_n0, c_r_n1, ...], [c_l_n0, ...]], [], []]
for _ in range(n_s):
    inp = sys.stdin.readline().strip()
    giri = enumerate(map(int, inp.split()))
    r_giri = filter(lambda x: not x[0] % 2, giri)
    c_r_giri = []
    c_r_n = 0
    for r_i, r_n in r_giri:
        c_r_n += r_n
        c_r_giri.append(c_r_n)

    giri = enumerate(map(int, inp.split()))
    l_giri = filter(lambda x: x[0] % 2, giri)
    c_l_giri = []
    c_l_n = 0
    for l_i, l_n in l_giri:
        c_l_n += l_n
        c_l_giri.append(c_l_n)

    c_giris.append([c_r_giri, c_l_giri])
print(c_giris)

# set init
tgt_idx = 0

for i in range(n_s):
    if tgt_idx < 13:   # left deck
        c_i = bisect(c_giris[i][1], tgt_idx)
        tgt_idx += c_giris[i][0][c_i]
        print("left", tgt_idx + 1)
    else:   # right deck
        c_i = bisect(c_giris[i][0], tgt_idx - 13)
        if c_i:
            tgt_idx += c_giris[i][1][c_i - 1] - 13
        else:
            tgt_idx += -13
        print("right", tgt_idx + 1)
