def solution(a, b):
    week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = 0
    for i in range (12):
        if(i != a-1):
            days += month[i]
        else:
            days += b
            break
    return week[days % 7]

print(solution(5, 24))