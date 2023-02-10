def solution(N, number):
    dp = [{}, {N}]
    if N == number:
        return 1
    for i in range(2, 9):
        answer_set = set()
        for j in range(1, i):
            for first in dp[j]:
                for second in dp[i-j]:
                    if first == int(str(N)*j) and second == int(str(N)*(i-j)):
                        answer_set.add(int(str(first) + str(second)))
                    answer_set.add(first + second)
                    answer_set.add(first - second)
                    answer_set.add(first * second)
                    if second != 0:
                        answer_set.add(first // second)
        if number in answer_set:
            return i
        dp.append(answer_set)
    return -1

N = 5
number = 12
print(solution(N, number))

print(int(str(N)*10))