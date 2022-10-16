def solution(n):
    answer = []
    stack = []
    while n > 0:
        stack.append(n % 10)
        n = n // 10
    while len(stack) == 0:
        answer.append(stack.pop())
    return answer

print(solution(12345))