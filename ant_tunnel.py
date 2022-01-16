import copy

i = int(input())

tunnel = []
for _ in range(i):
    tunnel.append(input().split()[1:])

tunnel.append(['APPLE', 'BANANA', 'YOGURT'])
tunnel.sort()
print(tunnel)
result = []

# 개선 가능
comparison = copy.deepcopy(tunnel)
for _ in range(1, i):
    for inner_idx in range(len(tunnel[_])):
        if comparison[_-1][inner_idx] == tunnel[_][inner_idx]:
            tunnel[_][inner_idx] = ''
        else:
            break

result = []
for _ in range(i):
    for inner_idx in range(len(tunnel[_])):
        if tunnel[_][inner_idx]:
            result.append('--'*inner_idx + tunnel[_][inner_idx])

print('\n'.join(result))

print(comparison[1][:1],comparison[2][:1])






