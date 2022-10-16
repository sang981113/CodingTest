def solution(absolutes, signs):
    answer = 0
    length = len(absolutes)
    for i in range(length):
        if(signs[i] == True):
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

def solution2(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
    
absolutes = [4,7,12]
signs = [True, False, True]
print(solution2(absolutes, signs))