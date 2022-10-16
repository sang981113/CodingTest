def solution(n):
    nums = []
    while n > 0:
        nums.append(str(n%10))
        n = n // 10
    nums.sort(reverse=True)
    return int(''.join(nums))

print(solution(118372))