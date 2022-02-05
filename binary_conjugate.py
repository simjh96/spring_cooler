n = int(input())
b = bin(n)[2:]
b = ''.join(['0' for _ in range(32-len(b))]) + b
bc = bin(2**32 - n)[2:]

result = 0
for _ in range(32):
    result += abs(int(bc[_]) - int(b[_]))

print(result)
