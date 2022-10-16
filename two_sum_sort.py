def solution(numbers):
    answer = []
    sum = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum.append(numbers[i] + numbers[j])
    answer = list(set(sum))
    answer.sort()
    return answer

numbers = [5,0,2,7]
print(solution(numbers))