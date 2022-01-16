n, d = map(int, input().split())
n = n + 1


def mod_change(_n, _d) -> list:
    rev_base = ''

    while _n > 0:
        _n, mod = divmod(_n, _d)
        rev_base += str(mod)

    return list(str(int(rev_base[::-1])))


m_n = mod_change(n, d)


def solution(m_n):
    if len(m_n) > d:
        return -1
    elif len(m_n) < d:
        result = [str(_) for _ in range(d)]
        result[0] = '1'
        result[1] = '0'
        return int(''.join(result), d)
    else:
        # check greater than max
        max_m_n = [str(_) for _ in list(range(d))[::-1]]
        if int(''.join(m_n)) > int(''.join(max_m_n)):
            return -1
        results = []
        _next_greatest(m_n, results)
        return int(''.join(next_greatest(m_n, results)), d)


def _next_greatest(m_n, results, idx=0):
    # m_n < d-1 d-2 .. 1 0
    if idx == d:
        return
    else:
        _result = m_n[idx]
        while _result in m_n[:idx]:
            _result = str((int(_result)+1) % d)
        results.append(_result)
        _next_greatest(m_n, results, idx+1)


def next_greatest(m_n, results):
    i = 1
    _results = results[:]
    print("m_n: ", m_n)
    while int(''.join(m_n)) > int(''.join(_results)):

        print(_results)
        _results[d-1-i:] = sorted(results[d-1-i:], reverse=True)
        print(_results)
        i += 1

    return _results







print(solution(m_n))









