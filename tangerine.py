def solution(k, tangerine):
    table = {}
    for size in tangerine:
        table.setdefault(size, 0)
        table[size] = table[size] + 1
    
    tuple_list = list(table.items())
    tuple_list.sort(key = lambda x : x[1], reverse=True)
    
    sum = 0
    for i in range(len(tuple_list)):
        sum += tuple_list[i][1]
        if sum >= k:
            return i+1

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))