def solution(k, d):
    count = 0
    y = d if d % k == 0 else d - d % k
    x = 0
    while x <= d:
        if x**2 + y**2 <= d**2:
            count += y//k + 1
            x += k
        else:
            y -= k
    return count

print(solution(2, 4))