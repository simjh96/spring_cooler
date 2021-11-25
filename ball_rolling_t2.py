from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)


N, M = map(int, input().split())
board = list()
P = dict()
udlr = defaultdict(dict)
d = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}
answer = [-1]


def get_end(p, drt):
    r, c = p[0], p[1]
    dr, dc = d[drt][0], d[drt][1]
    if board[r+dr][c+dc] == '#':
        udlr[drt][p] = [p, 0]  # memo
        return [p, 0]
    else:
        if (r, c) in udlr[drt]:
            return udlr[drt][(r, c)]
        else:
            _p, _dist = get_end((r+dr, c+dc), drt)
            udlr[drt][p] = [_p, _dist + 1]  # memo
            return [_p, _dist + 1]


# get R, B, O
for r in range(N):
    row = list(input())
    for c in range(M):
        if row[c] in ['R', 'B', 'O']:
            P[row[c]] = (r, c)
            row[c] = '.'
    board.append(row)

# set hole's position
udlr['u'][P['O']], udlr['d'][P['O']], udlr['l'][P['O']], udlr['r'][P['O']] \
    = [P['O'], 0], [P['O'], 0], [P['O'], 0], [P['O'], 0]

# set all position's u,d,l,r & dist
# hole's u,d,l,r == [hole's position, 0]
for r in range(N):
    for c in range(M):
        if board[r][c] != '#' and (r, c) != P['O']:
            get_end((r, c), 'u'), get_end((r, c), 'd'), get_end((r, c), 'l'), get_end((r, c), 'r')


# bfs
def bfs(r_b_ps, acts=0, visited=set()):
    if acts >= 10 or not r_b_ps:
        return
    else:
        visited |= r_b_ps  # memoize newly visited
        _r_b_ps = set()
        for r_b_p in r_b_ps:  # for all frontier get next frontier
            for drt in d:
                _r_p, _rd = udlr[drt][r_b_p[0]]
                _b_p, _bd = udlr[drt][r_b_p[1]]
                if _r_p == P['O'] and _b_p != P['O']:  # pivotal
                    answer[0] = acts + 1
                    return
                elif _b_p == P['O']:
                    continue

                if _r_p == _b_p:  # solve collapsed
                    if _rd > _bd:
                        _r_p = (_r_p[0] - d[drt][0], _r_p[1] - d[drt][1])
                    else:
                        _b_p = (_b_p[0] - d[drt][0], _b_p[1] - d[drt][1])
                _r_b_ps.add((_r_p, _b_p))
        _r_b_ps -= visited  # subtract visited from next frontier
        bfs(_r_b_ps, acts+1, visited)


bfs({(P['R'], P['B']), })
print(answer[0])



