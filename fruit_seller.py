def solution(k, m, score):
    score_dict = {}
    result = 0
    
    for i in range(k+1):
        score_dict[i] = 0
    
    for point in score:
        score_dict[point] += 1
    
    for i in range(k, 0, -1):
        count = score_dict[i]
        result += i * m * (count // m)
        
        if count % m != 0:
            score_dict[i-1] += count % m
        
    return result

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	
print(solution(k, m, score))