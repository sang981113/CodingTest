import re

def solution(dartResult):
    answer = 0
    before_point = 0
    point = 0
    list = re.findall('[0-9]{1,2}|[A-Z]|[*#]', dartResult)
    for item in list:
        if(re.match('[0-9]{1,2}', item)):
            answer += point
            before_point = point
            point = int(item)
        elif(re.match('[A-Z]', item)):
            if(item == 'S'):
                point = point ** 1
            elif(item == 'D'):
                point = point ** 2
            elif(item == 'T'):
                point = point ** 3
        else:
            if(item == '*'):
                point  = point * 2
                answer += before_point
            elif(item == '#'):
                point = -point

    answer += point
    return answer

def solution2(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

dartResult = "1S2D*3T"

print(solution(dartResult))