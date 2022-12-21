def solution(n , roads, sources, destination):
    memo = [-1 for _ in range(n+1)]
    memo[destination] = 0

    map = [[] for _ in range(n+1)]
    for a, b in roads:
        map[a].append(b)
        map[b].append(a)

    queue = [destination]

    while queue:
        now = queue.pop(0)
        for next in map[now]:
            if memo[next] == -1:
                queue.append(next)
                memo[next] = memo[now] + 1
    
    return [memo[source] for source in sources]

n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]
destination = 5
print(solution(n, roads, sources, destination))