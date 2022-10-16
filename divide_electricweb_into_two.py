def solution(n, wires):
    sub_list = []
    for i in range(n):
        sub_list.append(abs(2 * get_node_count(wires[:i] + wires[i+1:], 1) - n))
        print(sub_list)
    sub_list.sort()
    return sub_list[0]
    
    
def get_node_count(wires, start):
    sum = 0
    for i in range(len(wires)):
        if wires[i][0] == start:
            sum += get_node_count(wires[:i] + wires[i+1:], wires[i][1])
        elif wires[i][1] == start:
            sum += get_node_count(wires[:i] + wires[i+1:], wires[i][0])
    return sum+1

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))