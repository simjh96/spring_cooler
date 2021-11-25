import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

wave1, wave2, result = [1,2,2,1,1,2], [-2,-1], 2

cf = lcm(len(wave1), len(wave2))
f1 = len(wave1)
f2 = len(wave2)

flag = True
candidates = []
_fs = None
fvs = []

for i in range(max([f1, f2])):
    fv = 0
    for j in range(cf):
        fs = (wave1[(j+i) % f1] + wave2[j % f2])**2
        if j != 0:
            if fs != _fs:
                flag = False
        fv += fs
        _fs = fs
    if flag:
        fv = 0
    fvs.append(fv)







