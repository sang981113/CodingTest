def solution(arrayA, arrayB):
    gcd_A = arrayA[0]
    for num in arrayA:
        gcd_A = gcd(gcd_A, num)

    result_A = gcd_A
    for num in arrayB:
        if num % gcd_A == 0:
            result_A = gcd_A // gcd(num, gcd_A)
    
    gcd_B = arrayB[0]
    for num in arrayB:
        gcd_B = gcd(gcd_B, num)

    result_B = gcd_B
    for num in arrayA:
        if num % gcd_B == 0:
            result_B = gcd_B // gcd(num, gcd_B)
        
    if result_A > result_B:
        return result_A
    elif result_A == result_B:
        return 0
    else:
        return result_B


def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    return gcd(r, a)


assert solution([10, 17], [5, 20]) == 0, solution([10, 17], [5, 20])
assert solution([10, 20], [5, 17]) == 10, solution([10, 20], [5, 17])
assert solution([14, 35, 119], [18, 30, 102]) == 7, solution([14, 35, 119], [18, 30, 102])