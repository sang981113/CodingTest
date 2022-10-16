def solution(s):
    L = len(s)
    if(L % 2 == 0):
        answer = s[L//2-1:L//2+1:1]
    else:
        answer = s[L//2]
    return answer

def solution2(s):
    return s[(len(s)-1)//2:len(s)//2+1:1]
    
print(solution("abcde"))