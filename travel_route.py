def solution(tickets):
    answer = []
    tickets = sorted(tickets, key = lambda x: x[1])
    def dfs(tickets, travel_list, start):
        nonlocal answer
        travel_list.append(start)

        if(len(tickets) == 0):
            if(len(answer) != 0):
                for x, y in zip(answer, travel_list):
                    if(x < y):
                        return
            answer = travel_list
        
        for item in tickets:
            if(item[0] == start):
                copied_tickets = tickets.copy()
                copied_tickets.remove([start, item[1]])
                copied_answer = travel_list[:]
                dfs(copied_tickets, copied_answer, item[1])

    dfs(tickets, travel_list = [], start = "ICN")
    return answer

tickets = [['ICN','A'],['A','B'],['A','C'],['B','A'],['C','A']]
print(solution(tickets))