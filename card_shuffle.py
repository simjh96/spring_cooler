import sys


def cum_idx(tgt_idx: int, d_giri: list):
    # return deck idx containing tgt_idx
    cum = 0
    for d_i, d_n in d_giri:
        cum += d_n
        if tgt_idx < cum:
            return d_i


# set all input
n_s = int(sys.stdin.readline().strip())
giris = []   # [[[(0, r_n0), (2, r_n1), ...], [(1, l_n0), ...]], [], []]
for _ in range(n_s):
    inp = sys.stdin.readline().strip()
    giri = enumerate(map(int, inp.split()))
    r_giri = list(filter(lambda x: not x[0] % 2, giri))
    giri = enumerate(map(int, inp.split()))
    l_giri = list(filter(lambda x: x[0] % 2, giri))

    giris.append([r_giri, l_giri])
print(giris)

# set init
tgt_idx = 0

for i in range(n_s):
    if tgt_idx < 13:   # left deck
        front = 0
        c_i = cum_idx(tgt_idx, giris[i][1])
        for r_i, r_n in giris[i][0]:
            if r_i < c_i:
                front += r_n
            else:
                break
        tgt_idx = front + tgt_idx

    else:   # right deck
        front = 0
        c_i = cum_idx(tgt_idx - 13, giris[i][0])
        for l_i, l_n in giris[i][1]:
            if l_i < c_i:
                front += l_n
            else:
                break
        tgt_idx = front + tgt_idx - 13

print(tgt_idx + 1)
