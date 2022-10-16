def solution(queue1, queue2):
    queue = queue1 + queue2
    inner_sum = sum(queue1)
    outer_sum = sum(queue2)
    head = 0
    tail = len(queue1)
    count = 0
    while True:
        if inner_sum == outer_sum:
            return count
        elif inner_sum > outer_sum:
            inner_sum -= queue[head]
            outer_sum += queue[head]
            head = head + 1
            head = head % len(queue)
        else:
            inner_sum += queue[tail]
            outer_sum -= queue[tail]
            tail = tail + 1
            tail = tail % len(queue)
        count = count + 1
        if count > 2*len(queue):
            break
    return -1

queue1 = []
queue2 = []

print(solution(queue1, queue2))