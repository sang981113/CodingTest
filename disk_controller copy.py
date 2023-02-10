from heapq import heappush, heappop

def solution(jobs):
    time = 0
    delay_sum = 0
    early_heap = []
    ready_heap = []
    
    for start, duration in jobs:
        heappush(early_heap, (start, duration))
    
    while early_heap or ready_heap:
        while early_heap and early_heap[0][0] <= time:
            start, duration = heappop(early_heap)
            heappush(ready_heap, (duration, start))
        
        if ready_heap:
            duration, start = heappop(ready_heap)
            delay_sum += time - start + duration
            time += duration
        else:
            time = early_heap[0][0]

    return int(delay_sum/len(jobs))

if __name__ == '__main__':
    assert solution([[0, 3], [1, 9], [2, 6]]) == 9
    assert solution([[0, 3], [4, 3], [10, 3]]) == 3
    assert solution([[0, 10], [2, 3], [9, 3]]) == 9
    assert solution([[1, 10], [3, 3], [10, 3]]) == 9
    assert solution([[0, 10]]) == 10
    assert solution([[0, 10], [4, 10], [5, 11], [15, 2]]) == 15