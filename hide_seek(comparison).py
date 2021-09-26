import math
import sys
sys.setrecursionlimit(10**6)


def brute_force(dist: 'k-n**tel', tel: 'teleport usage', t_high=None):
    if dist == 0:
        return 0
    else:
        if t_high==None:
            t_high = tel
        binary_steps = dist//(2**tel)
        residual_dist = dist % (2**tel)
        if (t_high-tel == 3) and (binary_steps == 1):
            binary_steps = 0
        return brute_force(residual_dist, tel-1, t_high) + binary_steps


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


def contrast(s, ss):
    if s + ss:
        dp = [100000] * ((ss + s) * 2)
        dp[ss] = 0
        st = set([ss])
        for i in range(ss + s):
            newSet = set()
            while st:
                j = st.pop()
                if dp[j] == i:
                    if j > 0 and dp[j - 1] > i + 1:
                        dp[j - 1] = i + 1
                        newSet.add(j - 1)
                    if j + 1 < (ss + s) * 2 and dp[j + 1] > i + 1:
                        dp[j + 1] = i + 1
                        newSet.add(j + 1)
                    if j % 2 == 0 and dp[j // 2] > i + 1:
                        dp[j // 2] = i + 1
                        newSet.add(j // 2)

            st = newSet

            if dp[s] != 100000:
                break
        return dp[s]
    else:
        return 0


for me in range(100):
    for bro in range(100):
        my = hide_seek(me, bro)
        answer = contrast(me, bro)
        if my != answer:
            print(f'me : {me}')
            print(f'bro : {bro}')
            print(f'my : {my}')
            print(f'type(my) : {type(my)}')
            print(f'answer : {answer}')
            print(f'type(answer) : {type(answer)}')