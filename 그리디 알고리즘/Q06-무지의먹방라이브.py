# Q06-무지의 먹방 라이브


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    answer = 0
    food_length = len(food_times)
    while k > food_length:
        times = k // food_length
        k -= times * food_length
        for i in range(food_length):
            food_times[i] -= times
            if food_times[i] < 0:
                k -= food_times[i]
                food_times[i] = 0
    idx = 0
    while k > 0:
        if food_times[idx] > 0:
            k -= 1
            food_times[idx] -= 1
        idx += 1
        if idx == food_length:
            idx = 0
    while food_times[idx] == 0:
        idx += 1
        if idx == food_length:
            idx = 0
    answer = idx + 1
    return answer
