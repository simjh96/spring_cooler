from collections import defaultdict

n = input()
haves = input().split()
wants = input().split()

counts = defaultdict(int)
answer = 0

for h in haves:
    counts[h] += 1

for w in wants:
    if counts[w] > 0:
        counts[w] -= 1
    else:
        answer += 1

print(answer)