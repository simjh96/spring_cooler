n = int(input())
memo = set()
answer = []


def n_queen(progress=set(), initial=None, ban=set()):
    if len(progress) == n:
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

                    n_queen(progress | {(r, c)}, initial, ban_)


n_queen()

print(len(answer))
