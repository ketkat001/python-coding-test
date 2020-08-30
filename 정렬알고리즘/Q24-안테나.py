N = int(input())
house = list(map(int, input().split()))
house.sort()
if N % 2 == 0:
    answer_1, answer_2 = N // 2 - 1, N // 2
    ans1_sum, ans2_sum = 0, 0
    for i in range(N):
        ans1_sum += abs(house[i] - house[answer_1])
        ans2_sum += abs(house[i] - house[answer_2])
    if ans1_sum <= ans2_sum:
        answer = answer_1
    else:
        answer = answer_2
else:
    answer = N//2

print(house[answer])