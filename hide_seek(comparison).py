# import math
# import sys
# sys.setrecursionlimit(10**6)
#
#
# def brute_force(dist: 'k-n**tel', tel: 'teleport usage', t_high=None):
#     if dist == 0:
#         return 0
#     else:
#         if t_high==None:
#             t_high = tel
#         binary_steps = dist//(2**tel)
#         residual_dist = dist % (2**tel)
#         if (t_high-tel == 3) and (binary_steps == 1):
#             binary_steps = 0
#         return brute_force(residual_dist, tel-1, t_high) + binary_steps
#
#
# def hide_seek(n, k):
#     if k <= n:
#         return n-k
#
#     else:
#         steps = 0
#         if n == 0:
#             if k == 1:
#                 return steps + 1
#             else:
#                 n += 1
#                 steps += 1
#
#         t = math.floor(math.log(k // n, 2))
#         t_dist = k - (2 ** t) * n
#         t1_dist = (2 ** (t + 1)) * n - k
#         t_steps = brute_force(t_dist, t)
#         t1_steps = brute_force(t1_dist, t + 1)
#         steps = steps + t + min((t_steps, t1_steps + 1))
#
#         return steps

# def hide_seek(n, k):
#     steps = 0
#     if n >= k:
#         steps = n - k
#         return steps
#     if n == 0:
#         if k == 1:
#             n += 1
#             steps += 1
#             return steps
#         else:
#             n += 1
#             steps += 1
#
#     positions = {n}
#
#     half = 10**5//2
#
#     # 0 < n < k <= 10**5
#     while k not in positions:
#         # print(f'steps : {steps}')
#         # print(f'max position : {max(positions)}')
#         positions_ = set()
#
#         for vertex in positions:
#             positions_.add(vertex + 1)
#             if vertex >= 1:
#                 positions_.add(vertex - 1)
#             if vertex <= half:
#                 positions_.add(2*vertex)
#         steps += 1
#         positions = positions_
#
#     return steps

def hide_seek(n, k):
    steps = 0
    visited = {n}
    positions = {n}
    limit = 10**5

    while True:
        # print(f'steps : {steps}')
        # print(f'max position : {max(positions)}')
        positions_ = set()
        if k in visited:
            break

        for vertex in positions:
            if (vertex+1 not in visited) and (limit >= vertex + 1 >= 0):
                positions_.add(vertex + 1)
                visited.add(vertex + 1)
            if (vertex-1 not in visited) and (limit >= vertex - 1 >= 0):
                positions_.add(vertex - 1)
                visited.add(vertex - 1)
            if (vertex*2 not in visited) and (limit >= 2*vertex >= 0):
                positions_.add(2*vertex)
                visited.add(2*vertex)
        steps += 1
        positions = positions_

    return steps


def contrast(n, k):
    pass


for me in range(0, 110000, 10000):
    if me % 10 == 0:
        print(me//10)
    for bro in range(0, 110000, 10000):
        my = hide_seek(me, bro)
        answer = contrast(me, bro)

        if my != answer:
            print(f'me : {me}')
            print(f'bro : {bro}')
            print(f'my : {my}')
            print(f'type(my) : {type(my)}')
            print(f'answer : {answer}')
            print(f'type(answer) : {type(answer)}')