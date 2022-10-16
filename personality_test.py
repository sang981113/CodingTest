def solution(survey, choices):
    personality = dict()
    left = ['R', 'C', 'J', 'A']
    right = ['T', 'F', 'M', 'N']

    for i in range(4):
        personality[left[i]] = 0
        personality[right[i]] = 0
    
    for i in range(len(survey)):
        if choices[i] < 4:
            personality[survey[i][0]] = 4 - choices[i] + personality[survey[i][0]]
        else:
            personality[survey[i][1]] = choices[i] - 4 + personality[survey[i][1]]

    result = ''
    for i in range(4):
        if personality[left[i]] >= personality[right[i]]:
            result += left[i]
        else:
            result += right[i]

    return result

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))