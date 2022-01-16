from itertools import combinations

n = int(input())
A = map(int, input().split())
m = 1000000007

answer = 0
for i, j in combinations(A, 2):
    if answer > m:
        answer = answer % m
    answer += i*j

print(answer % m)


