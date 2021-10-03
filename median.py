import heapq
import sys


def find_median(new: int, max_heap=None, min_heap=None) -> '(max_heap, min_heap)':
    if max_heap is None:
        return [new], []
    else:
        total_len = len(max_heap) + len(min_heap) + 1

        if total_len % 2:
            if new > max_heap[0]:
                to_left = heapq.heappushpop(min_heap, new)
                max_heap.append(to_left)
                heapq._siftdown_max(max_heap, 0, len(max_heap) - 1)

            else:
                max_heap.append(new)
                heapq._siftdown_max(max_heap, 0, len(max_heap) - 1)

        else:
            if new > max_heap[0]:
                heapq.heappush(min_heap, new)

            else:
                old = heapq._heapreplace_max(max_heap, new)
                heapq.heappush(min_heap, old)


        return max_heap, min_heap


# max heap min heap
_max_heap = None
_min_heap = None

n = int(sys.stdin.readline().strip())

for _ in range(n):
    _new = int(sys.stdin.readline().strip())
    _max_heap, _min_heap = find_median(_new,_max_heap,_min_heap)
    print(_max_heap[0])

