def solution(triangle):
    dp = []
    for h in range(len(triangle)):
        if h == 0:
            dp.append(triangle[h])
            continue
        sum_floor = []
        for w in range(len(triangle[h])):
            if w-1 < 0:
                sum_floor.append(dp[h-1][w] + triangle[h][w])
            elif w+1 >= len(triangle[h]):
                sum_floor.append(dp[h-1][w-1] + triangle[h][w])
            else:
                sum_list = []
                if type(dp[h-1][w-1]) != list:
                    sum_list.append(dp[h-1][w-1] + triangle[h][w])
                else:
                    for sum in dp[h-1][w-1]:
                        sum_list.append(sum + triangle[h][w])
                if type(dp[h-1][w]) != list:
                    sum_list.append(dp[h-1][w] + triangle[h][w])
                else:
                    for sum in dp[h-1][w]:
                        sum_list.append(sum + triangle[h][w])
                sum_floor.append(sum_list)
        dp.append(sum_floor)
    
    floor_max = []
    for w in range(len(dp[-1])):
        if type(dp[-1][w]) != list:
            floor_max.append(dp[-1][w])
        else:
            floor_max.append(max(dp[-1][w]))
    
    return max(floor_max)

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))