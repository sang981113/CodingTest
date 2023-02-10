def solution(name):
    answer = 0
    alpha = 'A' * len(name)

    for i in range(len(name)):
        if alpha[i] != name[i]:
            diff = abs(ord(alpha[i]) - ord(name[i]))
            answer += diff if diff <= 13 else 26 - diff
    
    dist_list = []
    dist = 0
    for i in range(len(name)):
        if name[i] != 'A':
            dist_list.append(dist)
            dist = 0
        dist += 1
    dist_list.append(dist)
    start_dist = [0,0]
    if name[0] == 'A':
        start_dist = [dist_list[-1], dist_list[0]]
        dist_list = [dist_list[0] + dist_list[-1]] + dist_list[1:-1]

    dist_max = max(dist_list)
    reverse_list = [dist_list[0]] + dist_list[:0:-1]
    right = dist_list.index(dist_max)
    left = reverse_list.index(dist_max)

    right_sum = start_dist[1]
    for i in range(1, right):
        right_sum += dist_list[i]

    left_sum = start_dist[0]
    for i in range(1, left):
        left_sum += reverse_list[i]

    if left_sum > right_sum:
        dist = right_sum
    else:
        dist = left_sum

    if dist + len(name) - dist_max > len(name) - 1:
        answer += len(name) - 1
    else:
        answer += dist + len(name) - dist_max
    # answer += dist + len(name) - dist_max
    return answer


if True:
    assert solution("LABLPAJM") == 61, str(solution("LABLPAJM"))
    assert solution("BMOABA") == 30, str(solution("BMOABA"))
    assert solution("LAABAA") == 15, str(solution("LAABAA"))
    assert solution("AAAAAAAAJAAAA") == 14, str(solution("AAAAAAAAJAAAA"))
    assert solution("SAAAAAARRM") == 41, str(solution("SAAAAAARRM"))
    assert solution("RABAMATAWADLAFAVAAE") == 78, str(solution("RABAMATAWADLAFAVAAE"))
    assert solution("XAAAAAABA") == 6, str(solution("XAAAAAABA"))
    assert solution("AYOZAAVADAY") == 35, str(solution("AYOZAAVADAY"))
    assert solution("AAFEASAAVA") == 30, str(solution("AAFEASAAVA"))
    assert solution("UAGAAASAAFAFXZA") == 47, str(solution("UAGAAASAAFAFXZA"))
    assert solution("AAAAZAATAEA") == 19, str(solution("AAAAZAATAEA"))
    assert solution("AACALATLAHABAA") == 50, str(solution("AACALATLAHABAA"))
    assert solution("FAWJAAAFV") == 35, str(solution("FAWJAAAFV"))
    assert solution("AACAVAAPSAAOAA") == 49, str(solution("AACAVAAPSAAOAA"))
    assert solution("AKAAWAKX") == 33, str(solution("AKAAWAKX"))   
    assert solution("LOAAAHAJAAFAEBAWO") == 79, str(solution("LOAAAHAJAAFAEBAWO"))
    assert solution("ABABAAAAABA") == 10, str(solution("ABABAAAAABA"))
