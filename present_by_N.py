op = [' ', '+', '-', '*', '/']
br = ['(', ')']

def solution(N, number):
    dp = [[N]]


def tabulation(dp, N, number):
    if len(dp) > 8:
        return -1
    
    expr_list = []
    queue = []
    expr = ""

    while queue:
        expr = queue.pop(0)
        if len(expr) >= 2*N-1:
            continue

        


    dp.appned(expr_list)
    return memoization(dp, N, number)