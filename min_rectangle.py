def solution(sizes):
    answer = 0
    now = sizes[0]
    for size in sizes:
        if(max(now) < max(size)):
            if(now[0] < now[1]):
                now[1] = max(size)
            else:
                now[0] = max(size)
        if(min(now) < min(size)):
            if(now[0] < now[1]):
                now[0] = min(size)
            else:
                now[1] = min(size)
    answer = now[0] * now[1]
    return answer

def solution2(sizes):
    return max(max(size) for size in sizes) * max(min(size) for size in sizes)

print(solution2([[60, 50], [30, 70], [60, 30], [80, 40]]))