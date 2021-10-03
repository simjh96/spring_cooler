import sys

N = int(input())
# tree = {1:-1}
tree = dict()
isin_tree = {1: True}
for _ in range(N - 1):
    #     a, b = list(map(int, input().split()))
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))

    if a in isin_tree:
        tree[b] = a
        isin_tree[b] = True
    else:
        tree[a] = b
        isin_tree[a] = True

for _, v in sorted(tree.items()):
    print(v)