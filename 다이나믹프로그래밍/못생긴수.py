n = int(input())
dp = [0] * n
dp[0] = 1

a, b, c = 0, 0, 0  # 2, 3 ,5의 Index
next_a, next_b, next_c = 2, 3, 5  # 다음값들의 초기 값

for i in range(1, n):
    dp[i] = min(next_a, next_b, next_c)
    if dp[i] == next_a:  # 2의 곱인 경우
        a += 1
        next_a = dp[a] * 2
    if dp[i] == next_b: # 3의 곱인 경우
        b += 1
        next_b = dp[b] * 3
    if dp[i] == next_c:
        c += 1
        next_c = dp[c] * 5

print(dp)

