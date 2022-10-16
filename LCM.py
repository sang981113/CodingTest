def solution(arr):
    while len(arr) != 1:
        arr.append(lcm(arr.pop(0), arr.pop(0)))
    return arr[0]
    return 

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)

arr = [2,6,8,14]
print(solution(arr))