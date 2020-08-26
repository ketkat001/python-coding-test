from itertools import permutations


def solution(n, weak, dist):
    weak_len = len(weak)
    for i in range(weak_len):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    for start in range(weak_len):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            starting = weak[start] + friends[count-1]
            for pos in range(start, start+weak_len):
                if starting < weak[pos]:
                    count += 1
                    if count > len(dist):
                        break
                    starting = weak[pos] + friends[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer