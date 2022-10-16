def solution(n):
    answer = ''
    while(n > 0):
        if(n % 3 == 0):
            answer = '4' + answer
        elif(n % 3 == 1):
            answer = '1' + answer
            n += 2
        elif(n % 3 == 2):
            answer = '2' + answer
            n += 1
        n = (n - 3) // 3
    return answer

for i in range(1, 100):
    print(i, solution(i))
