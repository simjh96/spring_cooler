import math
n = int(input())
N = sorted([int(input()) for _ in range(n)])
dN = [N[_+1] - N[_] for _ in range(n-1)]
M = [_ for _ in range(2, N[1])]   # [2,3,...,N[1]-1]
out = set()
answer = []


def all_cd(arr):
    # cd of gcd
    gcd = arr[0]
    for _ in range(1, len(arr)):
        gcd = math.gcd(gcd, arr[_])
    print(f"    gcd : {gcd}")
    cd = []
    for _ in range(1, gcd+1):
        if gcd % _ == 0:
            cd.append(_)
    print(f"    all_cd : {cd}")
    return cd


for m in M:
    print(f"m:{m} - out:{out}===========")
    if m not in out:
        # check if m satisfy all dN
        divs = []
        for dn in dN:
            print(f"dn:{dn} % m:{m}")
            if dn % m:
                out |= set(range(m, N[1], m))
                break
            else:
                divs.append(dn//m)
        print(f"m: {m}")
        print(f"divs: {divs}")
        if len(divs) == n - 1:
            answer.extend([str(m*_) for _ in all_cd(divs)])
            out |= set(range(m, N[1], m))

print(' '.join(answer))
