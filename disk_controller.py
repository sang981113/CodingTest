import heapq

def solution(jobs):
    jobs.sort(key = lambda x: (x[0], x[1]))
    time = 0
    heap = []
    for i in range(jobs.size()):

        heapq.heappush(heap, jobs.pop(0))
    return

jobs = [[4, 3], [0, 3], [0, 1], [1, 9], [1, 2], [2, 6]]
heapq.heapify(jobs)
while jobs:
    print(heapq.heappop(jobs, 0))