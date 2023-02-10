def solution(topping):
    result = 0
    l_dict = {}
    r_dict = {}
    for top in topping:
        r_dict.setdefault(top, 0)
        r_dict[top] += 1
    for top in topping:
        l_dict.setdefault(top, 0)
        l_dict[top] += 1
        r_dict[top] -= 1
        if r_dict[top] == 0:
            del r_dict[top]
        if len(l_dict.keys()) == len(r_dict.keys()):
            result += 1
    return result
topping = [1,1,1,1,1,2,2,1]
print(solution(topping))