import math
import sys
sys.setrecursionlimit(10**6)


def brute_force(dist: 'k-n**tel', tel: 'teleport usage'):
    if dist == 0:
        return 0
    else:
        binary_steps = dist//(2**tel)
        residual_dist = dist % (2**tel)
        return brute_force(residual_dist, tel-1) + binary_steps


me, bro = map(int, input().split())


def hide_seek(n, k):
    if k <= n:
        return n-k

    else:
        steps = 0
        if n == 0:
            if k == 1:
                return steps + 1
            else:
                n += 1
                steps += 1

        t = math.floor(math.log(k // n, 2))
        t_dist = k - (2 ** t) * n
        t1_dist = (2 ** (t + 1)) * n - k
        t_steps = brute_force(t_dist, t)
        t1_steps = brute_force(t1_dist, t + 1)
        steps = steps + t + min((t_steps, t1_steps + 1))

        return steps


print(hide_seek(me, bro))

