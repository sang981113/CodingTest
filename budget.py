def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    while(len(d) > 0):
        if(sum + d[0] <= budget):
            sum += d.pop(0)
            answer += 1
        else:
            break

    return answer

d = [1,3,2,5,4]
budget = 9
print(solution(d, budget))