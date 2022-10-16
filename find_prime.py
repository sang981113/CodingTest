def solution(n):
    prime_arr = [2]
    for i in range(3, n+1):
        for prime in prime_arr:
            if i % prime == 0:
                break
            if i // prime < 2:
                prime_arr.append(i)
                break
    return len(prime_arr)

print(solution(20))