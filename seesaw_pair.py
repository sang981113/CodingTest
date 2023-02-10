from collections import defaultdict
import math

def nCr(n, r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

def solution(weights):
    result = 0
    weights_dict = defaultdict(lambda: 0)
    for weight in weights:
        weights_dict[weight] += 1
    
    for weight in weights_dict.keys():
        if weights_dict[weight] > 1:
            result += nCr(weights_dict[weight], 2)
        
        if weight * 2 in weights_dict.keys():
            result += weights_dict[weight] * weights_dict[weight * 2]
        
        if weight * 3 / 2 in weights_dict.keys():
            result += weights_dict[weight] * weights_dict[weight * 3 / 2]
        
        if weight * 4 / 3 in weights_dict.keys():
            result += weights_dict[weight] * weights_dict[weight * 4 / 3]

    return result

weights = [100,180,360,100,270]
print(solution(weights))
            

"""
    combinations of (2,3,4)
    (2,3), (2,4), (3,4)
"""