import sys


def gcd(a, b, v):
    if v.get((max([a,b]), min([a,b]))):
        return v.get((max([a,b]), min([a,b])))

    if a >= b:
        if a % b == 0:
            v[(a, b)] = b
            return b
        else:
            v[(a, b)] = gcd(b, a % b, v)
            return v[(a, b)]
    else:
        if b % a == 0:
            v[(b, a)] = a
            return a
        else:
            v[(b, a)] = gcd(a, b % a, v)
            return v[(b, a)]


v = dict()
N = int(input())
arr = list()
for _ in range(N):
    #     arr.append(int(input()))
    arr.append(int(sys.stdin.readline().rstrip()))

arr = sorted(arr)
diffs = [arr[i + 1] - arr[i] for i in range(N - 1)]
# diffs = [j - i for i, j in zip(arr, arr[1:])]
for _ in range(N - 2):
    diffs = [gcd(diffs[i], diffs[i + 1], v) for i in range(len(diffs) - 1)]
#     diffs = [gcd(i, j, v) for i, j in zip(diffs, diffs[1:])]

tar = diffs.pop()
for i in range(2, tar + 1):
    if tar % i == 0:
        print(i, end=" ")
