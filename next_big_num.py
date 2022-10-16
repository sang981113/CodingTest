def solution(n):
    one_count = get_binary(n).count('1')
    n += 1
    while one_count != get_binary(n).count('1'):
        n += 1
    return n

def get_binary(decimal):
    result = ''
    while decimal != 0:
        result = str(decimal % 2) + result
        decimal = decimal // 2
    return result

print(solution(78))