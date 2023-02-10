from collections import defaultdict

def solution(x, y, n):
    queue = [x]
    cnt_dict = defaultdict(lambda: -1)
    cnt_dict[x] += 1

    while queue:
        x = queue.pop(0)

        if cnt_dict[x] > 0:
            continue

        if x + n < y:
            queue.append(x + n)
            cnt_dict[x + n] = cnt_dict[x] + 1
            
        if 2 * x < y:
            queue.append(2 * x)
            cnt_dict[2 * x] = cnt_dict[x] + 1

        if 3 * x < y:
            queue.append(3 * x)
            cnt_dict[3 * x] = cnt_dict[x] + 1
    return cnt_dict[y]

x = 10
y = 20
n = 5

print(solution(x, y, n))