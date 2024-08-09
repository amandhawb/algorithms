import heapq
from operator import neg


def last_stone_weight(stones):
    heap = [-stone for stone in stones]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        # obtain two largest stones
        stone1 = heapq.heappop(heap)
        stone2 = heapq.heappop(heap)

        # smash the two stones
        result = abs(stone2 - stone1)

        if result == 0:
            continue
        else:
            heapq.heappush(heap, result)

    if len(heap) == 1:
        return heap[0]
    else:
        return 0
    
print('input', [2,2])
print('output', last_stone_weight([2,2]))

print('input', [2,7,4,1,8,1])
print('output', last_stone_weight([2,7,4,1,8,1]))