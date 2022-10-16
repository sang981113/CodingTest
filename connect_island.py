def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    island_set = [i for i in range(n)]
    result = 0
    while not all_same_element(island_set):
        if len(costs) == 0:
            return -1
        now_island = costs.pop(0)
        result += union_find(island_set, now_island)

    return result

def union_find(list, edge):
    if list[edge[0]] == list[edge[1]]:
        return 0
    if list[edge[0]] < list[edge[1]]:
        another = list[edge[1]]
        for i in range(len(list)):
            if list[i] == another:
                list[i] = list[edge[0]]
    else:
        another = list[edge[0]]
        for i in range(len(list)):
            if list[i] == another:
                list[i] = list[edge[1]]
    return edge[2]

def all_same_element(list):
    for i in range(len(list)):
        if list[i] != list[0]:
            return False
    return True

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))