import sys
# 자료 구조를 merge 하기 좋은걸로 바꿔야할듯


n = int(sys.stdin.readline().strip())
panels = []
for _ in range(n):
    panels.append(list(map(int, sys.stdin.readline().strip().split())))
panels.sort(key=lambda x: x[0])


def merge(ps: list):
    # merge all while there is merge
    i = 0
    j = 0
    blocks = [ps[i]]
    while i < len(ps) - 1:
        i += 1
        if blocks[j][1] >= ps[i][0]:   # overlapping -> extend
            blocks[j][1] = max(ps[i][1], blocks[j][1])
        else:   # non overlapping -> new
            j += 1
            blocks.append(ps[i])
    return blocks


merged0 = merge(panels)
ext = list(map(lambda x: [x[0], x[1], 2*x[1] - x[0]], merged0))   # extended
# print(merged0)
# print(extended)

# merge all while there is merge
i = 0
j = 0
blocks = [ext[i]]
while i < len(ext) - 1:
    i += 1
    if blocks[j][2] >= ext[i][0]:  # reachable -> reach
        blocks[j][1], blocks[j][2] = max(ext[i][1], blocks[j][1]), max(ext[i][2], blocks[j][2])
    else:  # no more reach ables
        break
# print(ext)
print(blocks[0][1])


