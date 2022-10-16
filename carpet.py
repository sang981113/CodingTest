def solution(brown, yellow):
    yellow_divisor = []
    for i in range(1, int(yellow**0.5)+1):
        if(yellow % i == 0):
            yellow_divisor.append(list([i, yellow//i]))
    
    for yellow_size in yellow_divisor:
        side1 = yellow_size.pop()
        side2 = yellow_size.pop()
        if(brown == side1*2 + side2*2 + 4):
            return [max(side1, side1)+2, min(side1, side2)+2]

print(solution(24, 24))