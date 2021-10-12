n, m = map(int, input().split())
up_to_n = list(range(1, n+1))

result = []


def up_to_m(n_arr, i=0, m_arr=[], level=0, debug=0) -> 'void':
    debug += 1
    print('======================================================')
    print(' ' * debug + f'n_arr:{n_arr}')
    print(' ' * debug + f'i:{i}')
    print(' ' * debug + f'm_arr:{m_arr}')
    print(' ' * debug + f'level:{level}')
    if (m-level)+i > n:
        print(' '*debug+f'(m-level)+i:{(m-level)+i} > n:{n}')
        return
    else:
        if len(m_arr) == m:
            print(' ' * debug + f'len(m_arr) == m:{m}')
            result.append(' '.join(map(str, m_arr)))
            return
        else:
            print(' ' * debug + f'len(m_arr):{len(m_arr)} != m:{m}')
            for _ in range(i, n):
                up_to_m(n_arr, i + 1, m_arr + [n_arr[i]], level + 1, debug)
                i += 1


up_to_m(up_to_n)
print('\n'.join(result))
