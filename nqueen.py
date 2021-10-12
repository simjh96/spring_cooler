n = int(input())
memo = set()
answer = []


def n_queen(progress=set(), initial=None, ban=set(), debug=0):
    print('===============================')
    board = [[0 for _ in range(n)] for _ in range(n)]
    for b_r, b_c in ban:
        if 0 <= b_r <= n-1 and 0 <= b_c <= n-1:
            board[b_r][b_c] = 2
    for p_r, p_c in progress:
        board[p_r][p_c] = 1
    [print(' '*debug + f'{r}') for r in board]
    print(' ' * debug + f'len={len(progress)}')
    print(' '*debug + f'initial={initial}')
    # print(' '*debug + f'answer={answer}')
    debug += 1
    if len(progress) == n:
        print(' '*debug + f'len(progress) == n')
        memo.add(initial)
        if progress not in answer:
            answer.append(progress)

    else:
        for r in range(n):
            for c in range(n):
                if ((r, c) in ban) or ((r, c) in memo):
                    pass
                else:
                    if initial is None:
                        initial = (r, c)
                    ban_ = ban.copy()
                    [ban_.add((r_, c)) for r_ in range(n)]
                    [ban_.add((r, c_)) for c_ in range(n)]
                    [ban_.add((r+d, c+d)) for d in range(n)]
                    [ban_.add((r-d, c-d)) for d in range(n)]
                    [ban_.add((r+d, c-d)) for d in range(n)]
                    [ban_.add((r-d, c+d)) for d in range(n)]

                    n_queen(progress | {(r, c)}, initial, ban_, debug)


n_queen()

print(answer)