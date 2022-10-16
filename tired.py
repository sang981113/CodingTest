def solution(k, dungeons):
    answer = 0
    def dfs(k, dungeons, result):
        nonlocal answer
        if(len(dungeons) == 0 or k == 0):
            if(answer == 0 or answer < result):
                answer = result

        for dungeon in dungeons:
            copied_dungeons = dungeons.copy()
            copied_dungeons.remove(dungeon)
            if(k >= dungeon[0] and k >= dungeon[1]):
                dfs(k - dungeon[1], copied_dungeons, result+1)
            else:
                dfs(k , copied_dungeons, result)
    dfs(k, dungeons, 0)
    return answer

solution2 = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))
print(solution2(k, dungeons))
