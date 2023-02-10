def solution(cap, n, deliveries, pickups):
    deliveries_sum = sum(deliveries)
    pickups_sum = sum(pickups)
    #일단 최대 cap을 가지고 맨끝 노드부터 앞에 있는 노드 순으로 택배를 전달(역순으로 배달)
    if deliveries_sum // cap > 0:
        now_cap = cap
    else:
        now_cap = deliveries_sum % cap
    deliveries_sum -= now_cap
    for i in range(n-1, -1, -1):
        if now_cap == 0:
            break
        if deliveries[i] <= now_cap:
            now_cap -= deliveries[i]
            deliveries[i] = 0
        else:
            deliveries[i] -= now_cap
    
    #최대 cap의 빈 택배 상자를 역순으로 회수