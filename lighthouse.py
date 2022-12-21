def solution(n, lighthouse):
    count = 0
    map = [[0 for _ in range(n+1)] for _ in range(n+1)]
    light = [0 for _ in range(n+1)]
    queue = [1]

    for num1, num2 in lighthouse:
        map[num1][num2] = 1
        map[num2][num1] = 1

    while queue:
        pos = queue.pop(0)
        if map[pos].count(1) == 0:
            continue
        if light[pos] == 1:
            for i in range(1, len(light)):
                if map[pos][i] == 1:
                    map[pos][i] = 0
                    map[i][pos] = 0
                    queue.append(i)
            continue
        if is_leaf(map, pos) == True:
            moved = map[pos].index(1)
            map[pos][moved] = 0
            map[moved][pos] = 0
            light[moved] = 1
            queue.append(moved)
        else:
            queue.append(pos+1)
    return light

def is_leaf(map, pos):
    if map[pos].count(1) == 1:
        return True
    else:
        return False

n = 11
Lighthouse = [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8], [6, 9],[7, 10],[8, 11]]

print(solution(n, Lighthouse))