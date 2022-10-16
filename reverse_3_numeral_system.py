def solution(n):
    answer = 0
    list = []
    while(n > 0):
        list.append(n%3)
        n = n//3
    while(len(list) > 0):
        answer += 3**len(list)//3 * list.pop(0)
    return answer

print(solution(45))