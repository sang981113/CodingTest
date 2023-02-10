from heapq import heappush, heappop

def solution(jobs):
    time = 0
    delay_sum = 0
    ready_heap = []
    sorted_jobs = sorted(jobs, key=lambda x: x[0])
    
    while sorted_jobs or ready_heap:
        while sorted_jobs and sorted_jobs[0][0] <= time:
            start, duration = sorted_jobs.pop(0)
            heappush(ready_heap, (duration, start))
        
        if ready_heap:
            duration, start = heappop(ready_heap)
            delay_sum += time - start + duration
            time += duration
        else:
            time = sorted_jobs[0][0]

    return int(delay_sum/len(jobs))