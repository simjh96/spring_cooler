import sys
sys.setrecursionlimit(10**9)

def get_a(t):
    if t//(30*12):
        if (t//(30*12)) % 2:
            return get_a(t - 30*12) + 1
        else:
            return get_a(t - 30*12)
    else:
        return -1


s = list(map(int, input().split()))
e = list(map(int, input().split()))

t = ((e[0]-1)*30*12 + (e[1]-1)*30 + e[2]) - ((s[0]-1)*30*12 + (s[1]-1)*30 + s[2])

m = t//30
y = t//(30*12)*15 + max([0, get_a(t)])

print(y, m, t)

