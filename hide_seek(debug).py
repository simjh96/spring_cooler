import math
import sys
sys.setrecursionlimit(10**6)

# t+1에서 남은 길이가 (n-1)*2**h 보다 큰 경우
def brute_force(dist: 'k-n**tel', tel: 'teleport usage'):
    if dist == 0:
        print('  '*tel + f'reached destination!')
        return 0
    else:
        binary_steps = dist//(2**tel)
        residual_dist = dist % (2**tel)
        print('  '*tel + f'  tel : {tel}')
        print('  '*tel + f'  binary_steps : {binary_steps}')
        print('  '*tel + f'  residual_dist : {residual_dist}')
        return brute_force(residual_dist, tel-1) + binary_steps


n, k = map(int, input().split())


def hide_seek(n, k):
    if k <= n:
        steps = n-k
        print(f'k is behind n!')
        print(f'n : {n}')
        print(f'k : {k}')
        print(f'steps : {steps}')
        return steps
    else:
        steps = 0
        if n == 0:
            if k == 1:
                steps += 1
                return steps
            else:
                n += 1
                steps += 1
                print(f'n is 0!')
                print(f'n : {n}')
                print(f'k : {k}')
                print(f'steps : {steps}')

        t = math.floor(math.log(k//n, 2))
        t_dist = k - (2**t)*n
        t1_dist = (2**(t+1))*n - k
        print(f't : {t}')
        print(f't_dist : {t_dist}')
        print(f't1_dist : {t1_dist}')

        # max(brute(t),brute(t+1))
        print(f't_steps')
        t_steps = brute_force(t_dist, t)

        print(f't1_steps')
        t1_steps = brute_force(t1_dist, t+1)

        print(f'final t_steps : {t_steps}')
        print(f'final t1_steps : {t1_steps}')
        steps += t + min((t_steps, t1_steps + 1))
        print(f'final steps : {steps}')
        return steps

print(hide_seek(n, k))