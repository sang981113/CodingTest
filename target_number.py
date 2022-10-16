def dfs(numbers, target, sign, pos, sum):
    if(pos >= len(numbers)):
        print("pos >= len(numbers)", pos, len(numbers), sum)
        if(sum == target):
            return 1
        else:
            return 0
    
    sum += sign * numbers[pos]

    return dfs(numbers, target, 1, pos+1, sum) + dfs(numbers, target, -1, pos+1, sum)

def solution(numbers, target):
    return (dfs(numbers, target, 1, 0, 0) + dfs(numbers, target, -1, 0, 0))/2

numbers = [4, 1, 2, 1]
target = 4

print(solution(numbers, target))