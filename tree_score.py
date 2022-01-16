import sys

N, Q = map(int, sys.stdin.readline().strip().split())
Ps = list(map(int, sys.stdin.readline().strip().split()))
Xs = []
for _ in range(Q):
    Xs.append(int(sys.stdin.readline().strip()))

# if X < Ps[0]: special case
# else: sum((i+1)*d_i; i==k-1) + (X - P_k)*(k+1) + (P_k+1 - X)*(N - (k+1)) + sum((N-(k+1+i))*d_k+i; k+i==N-2)
ds = [Ps[i] - Ps[i - 1] for i in range(1, len(Ps))]  # [d1, d2, d3 ..., d(N-1)]


def binary_search(tgt, Ps):
    left = 0
    right = len(Ps) - 1
    while left <= right:
        mid = (left + right) // 2
        if Ps[mid] > tgt:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer


def get_score(x, ds, Ps):
    k = binary_search(x, Ps)
    front = sum([(i + 1) * ds[i] for i in range(k)]) + (x - Ps[k]) * (k + 1)
    # print(f'front: {front}')
    if k+1 <= N-1:
        end = (Ps[k + 1] - x) * (N - (k + 1)) + sum([(N - (i + 1)) * ds[i] for i in range(k + 1, N - 1)])
        front += end
        # print(f'end: {end}')
    return front


for x in Xs:
    if x < Ps[0]:
        print((Ps[0] - x) * N + sum([(N - (i + 1)) * ds[i] for i in range(N - 1)]))
    else:
        print(get_score(x, ds, Ps))
