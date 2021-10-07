import math
import sys


def get_potential(x0, y0, r0, x1, y1, r1):
    potential = None

    # distance
    dist = round(math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2), 10)

    # identical
    if (x0, y0, r0) == (x1, y1, r1):
        potential = -1

    # inside
    elif dist + min(r0, r1) < max(r0, r1):
        potential = 0

    # apart
    elif r0 + r1 < dist:
        potential = 0

    # tangent
    elif float(r0 + r1) == float(dist) or float(dist + min(r0, r1)) == float(max(r0, r1)):
        potential = 1

    else:
        potential = 2

    return potential


# input
p = int(sys.stdin.readline())
for _ in range(p):
    x0, y0, r0, x1, y1, r1 = map(int, sys.stdin.readline().strip().split())
    print(get_potential(x0, y0, r0, x1, y1, r1))
