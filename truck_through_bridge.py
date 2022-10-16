def solution(bridge_length, weight, truck_weights):
    weights = truck_weights[:]
    truck_pos = []
    in_bridge = []
    arrive = []
    time = 0
    while len(arrive) != len(truck_weights):
        time += 1
        sub_all_value(truck_pos, 1)
        if len(truck_pos) > 0 and truck_pos[0] == 0:
            truck_pos.pop(0)
            arrive.append(in_bridge.pop(0))
        
        if len(weights) > 0 and weight < sum(in_bridge) + weights[0]:
            continue
            
        if len(weights) > 0: 
            in_bridge.append(weights.pop(0))
            truck_pos.append(bridge_length)
        
    return time
        
def sub_all_value(num_array, sub_value):
    for i in range(len(num_array)):
        num_array[i] = num_array[i] - sub_value

bridge_length = 100
weight = 100
truck_weights = [10]

print(solution(bridge_length, weight, truck_weights))