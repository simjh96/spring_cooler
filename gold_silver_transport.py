# a, b, g, s, w, t = 10, 10, [100], [100], [7], [10]


# T_g, last_s = get_T(a, g)
# T_s, last_g = get_T(b, s)
# print(f'T_g, last_s: {T_g, last_s}')
# print(f'T_s, last_g: {T_s, last_g}')
# if T_g <= T_s:
#     print('=========T_g <= T_s=========')
#     s_, b_ = last_clearing(last_s, s, b)

#     buffer_s, depleted = get_buffer(s_, g, T_g)
#     print(f'b_, buffer_s, depleted : {b_, buffer_s, depleted}')
#     print(get_T(b_-buffer_s, depleted)[0])
#     if buffer_s >= b_:
#         print(T_g)
#     else:
#         print('===================')
#         late = get_T(a, g, False)[0]
#         print('===================')
#         print(late + get_T(b_-buffer_s, depleted)[0])


def solution(a, b, g, s, w, t):
    def get_rounds(T, t0, last=True):
        # get number of visits made in T
        return (T // t0) // 2 + ((T // t0) % 2) * int(last)

    def get_T(target, material, last=True) -> 'T_m, [last_scoop, distributable]':
        left = 0
        right = ((a + b) // min(w) + 1) * (max(t) * 2)
        while left <= right:
            mid = left + (right - left) // 2
            obtained = sum([min([material[_], get_rounds(mid, t[_], last) * w[_]]) for _ in range(len(material))])
            if obtained >= target:
                right = mid - 1
            else:
                left = mid + 1

        # print(f'obtained, mid : {obtained, mid}')
        if obtained < target:
            T_m = mid + 1
        else:
            T_m = mid

        last_scoop = sum([min([material[_], get_rounds(T_m, t[_]) * w[_]]) for _ in range(len(material))]) - target
        distributable = [bool(get_rounds(T_m, t[_])) for _ in range(len(material))]
        return T_m, [last_scoop, distributable]

    def get_buffer(l_m, s_m, s_T) -> '(buffer, depleteds)':
        depleteds = []
        buffer = 0
        for _ in range(len(s_m)):
            # minning from depleted
            obtained = max([get_rounds(s_T, t[_]) * w[_] - s_m[_], 0])
            obtained = min([obtained, l_m[_]])

            buffer += obtained
            depleteds.append(l_m[_] - obtained)
        return buffer, depleteds

    def last_clearing(last_m, m, target) -> 'm, target':
        last_m, m, target = last_m.copy(), m.copy(), target

        before = 1
        after = -1
        while before != after:
            before = last_m[0]
            for _ in range(len(s)):
                if last_m[1][_]:
                    if m[_] > 0 and last_m[0] > 0:
                        m[_] -= 1
                        target -= 1
                        last_m[0] -= 1
                        # print(f'm : {m}, target : {target}, last_m : {last_m}')
            after = last_m[0]
        return m, target

    # T_g
    T_g, last_s = get_T(a, g)
    T_s, last_g = get_T(b, s)
    # print(f'T_g, last_s: {T_g, last_s}')
    # print(f'T_s, last_g: {T_s, last_g}')
    if T_g <= T_s:
        # print('=========T_g <= T_s=========')
        s_, b_ = last_clearing(last_s, s, b)
        buffer_s, depleted = get_buffer(s_, g, T_g)
        # print(f'b_, buffer_s, depleted : {b_, buffer_s, depleted}')
        # print(get_T(b_-buffer_s, depleted)[0])
        if buffer_s >= b_:
            return T_g
        else:
            return get_T(a, g, False)[0] + get_T(b_ - buffer_s, depleted)[0]

    else:
        # print('=========T_g > T_s=========')
        g_, a_ = last_clearing(last_g, g, a)
        buffer_g, depleted = get_buffer(g_, s, T_s)
        # print(f'a_, buffer_g, depleted : {a_, buffer_g, depleted}')
        if buffer_g >= a_:
            return T_s
        else:
            return get_T(b, s, False)[0] + get_T(a_ - buffer_g, depleted)[0]



# 중도 포기`