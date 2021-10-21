import sys

sys.setrecursionlimit(10 ** 6)

m, n = map(int, sys.stdin.readline().strip().split())
nodes = []
for _ in range(n):
    nodes += list(map(int, sys.stdin.readline().strip().split()))

visited = set()
rotten = set([_ for _ in range(len(nodes)) if nodes[_] == 1])
counts = [-1]
full = sum(map(lambda x: x != -1, nodes))


def bfs(front_line, i=0):
    print(f'front_line:{front_line}')
    # end with full visit
    if len(front_line) == 0:
        if full == len(visited):
            counts[0] = i - 1
    else:
        front_line_ = set()
        [visited.add(_) for _ in front_line]
        for j in front_line:
            # 상하좌우로 존재하며 -1 아니며 visited 안한곳
            if (0 <= j - m and nodes[j - m] != -1) and ((j - m) not in visited):
                print(f'((j:{j} - m:{m}) not in visited):{((j - m) not in visited)}')
                front_line_.add(j - m)
            if (j + m < m * n and nodes[j + m] != -1) and ((j + m) not in visited):
                print(f'((j:{j} + m:{m}) not in visited):{((j + m) not in visited)}')
                front_line_.add(j + m)
            if (j + 1 < m * n and (j + 1) % m) and (nodes[j + 1] != -1 and ((j + 1) not in visited)):
                print(f'((j:{j} + 1) not in visited):{((j + 1) not in visited)}')
                front_line_.add(j + 1)
            if (0 <= j - 1 and j % m) and (nodes[j - 1] != -1 and ((j - 1) not in visited)):
                print(f'((j:{j} - 1) not in visited):{((j - 1) not in visited)}')
                front_line_.add(j - 1)

        bfs(front_line_, i + 1)


bfs(rotten)
print(counts[0])
