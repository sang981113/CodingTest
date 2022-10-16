def solution(rows, columns, queries):
    array = [[i+(columns*j) for i in range(1, columns+1)] for j in range(rows)]
    answer = []
    for query in queries:
        queue = []
        spin_elements = []
        queue.append(array[query[0]-1][query[1]-1])
        spin_elements.append(array[query[0]-1][query[1]-1])
        for y in range(query[1], query[3]):
            queue.append(array[query[0]-1][y])
            spin_elements.append(array[query[0]-1][y])
            array[query[0]-1][y] = queue.pop(0)
        for x in range(query[0], query[2]):
            queue.append(array[x][query[3]-1])
            spin_elements.append(array[x][query[3]-1])
            array[x][query[3]-1] = queue.pop(0)
        for y in range(query[3]-2, query[1]-2, -1):
            queue.append(array[query[2]-1][y])
            spin_elements.append(array[query[2]-1][y])
            array[query[2]-1][y] = queue.pop(0)
        for x in range(query[2]-2, query[0]-2, -1):
            queue.append(array[x][query[1]-1])
            spin_elements.append(array[x][query[1]-1])
            array[x][query[1]-1] = queue.pop(0)
        answer.append(min(spin_elements))
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))