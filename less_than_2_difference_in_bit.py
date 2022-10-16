def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = get_binary(number)
        i = number+1
        while True:
            if compare_binary(bin_number, get_binary(i)) <= 2:
                answer.append(i)
                break
            i += 1
    return answer
        
def get_binary(number):
    bin_number = ''
    while number > 0:
        bin_number = bin_number + str(number%2)
        number = number//2
    return bin_number[::-1]

def compare_binary(bin1, bin2):
    cnt = 0
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.rjust(max_len, '0')
    bin2 = bin2.rjust(max_len, '0')
    for i in range(max_len):
        if bin1[i] != bin2[i]:
            cnt += 1
    return cnt

numbers = [2,7]
print(solution(numbers))