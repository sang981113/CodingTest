def solution(begin, end):
    answer = [0 for i in range(end+1)]
    maximum = 10000000
    if end < maximum:
        maximum = end
    for i in range(maximum, 0, -1):
        multiplier = 2
        while i * multiplier <= end:
            if answer[i*multiplier] == 0:
                answer[i*multiplier] = i
            multiplier += 1
    return answer[begin:end+1]

def solution2(begin, end):
    answer = [0 for i in range(end+1)]
    for i in range(1, 10000001):
        multiplier = 2
        while i * multiplier <= end:
            answer[i*multiplier] = i
            multiplier += 1
    return answer[begin:end+1]

begin = 1
end = 10
print(solution2(begin, end))