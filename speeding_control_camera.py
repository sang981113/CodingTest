import heapq

def solution(routes):
    out_list = []
    count = 0
    routes.sort(key=lambda x: x[0])
    heapq.heappush(out_list, routes.pop(0)[1])
    while routes:
        route = routes.pop(0)
        now_in = route[0]
        now_out = route[1]
        if out_list[0] < now_in:
            out_list.clear()
            count += 1
        heapq.heappush(out_list, now_out)
    if len(out_list) > 0:
        out_list.clear()
        count += 1
    return count

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))