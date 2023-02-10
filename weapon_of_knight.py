def solution(number, limit, power):
    result = 0
    
    for i in range(1, number+1):
        weight = get_divisor(i)
        if weight > limit:
            result += power
        else:
            result += weight
    return result

def get_divisor(num):
    cnt = 0

    if num ** 0.5 == int(num ** 0.5):
        cnt -= 1

    for i in range(1, int(num ** 0.5)+1):
        if num % i == 0:
            cnt += 2
    
    return cnt

number = 5
limit = 3
power = 2
print(solution(number, limit, power))