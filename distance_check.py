def solution(places):
    def dfs(place, pos_x, pos_y, dist):
        nonlocal is_find
        if dist <= 0:
            return 1
        for dx, dy in zip(x, y):
            if pos_x+dx < 0 or pos_y+dy < 0 or pos_x+dx >= len(place[0])-1 or pos_y+dy >= len(place)-1:
                continue
            if place[pos_x+dx][pos_y+dy] == 'P':
                is_find = True
                return 0
            elif place[pos_x+dx][pos_y+dy] == 'X':
                continue
            elif place[pos_x+dx][pos_y+dy] == 'O':
                tmp_list = list(place[pos_x])
                tmp_list[pos_y] = 'O'
                place[pos_x] = ''.join(tmp_list)
                dfs(place, pos_x+dx, pos_y+dy, dist-1)
    answer = []
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    is_find = False
    for place in places:
        for i in range(len(place)):
            answer_copy = answer[:]
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    dfs(place, i, j, 2)
                    if is_find == True:
                        answer.append(0)
                        is_find = False
                        break
            if answer_copy != answer:
                break
        if len(answer)-1 != places.index(place):
            answer.append(1)
    return answer

places =  [["POOOP", 
            "OXPXX",
            "OPXPX",
            "OOXOX",
            "OPXXP"]]
print(solution(places))