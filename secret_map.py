def solution(n, arr1, arr2):
    answer = []
    for l1, l2 in zip(arr1, arr2):
        str = ""
        for i in range(n):
            if(l1 % 2 == 1 or l2 % 2 == 1):
                str += "#"
            else:
                str += " "
            l1 = l1 // 2
            l2 = l2 // 2
        answer.append(str[::-1])
    return answer

def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
result = solution(n, arr1, arr2)
for i in result:
    print(i)