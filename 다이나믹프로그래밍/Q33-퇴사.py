n = int(input())
day = []
value = []
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    a, b = map(int, input().split())
    day.append(a)
    value.append(b)

for i in range(n-1, -1, -1):
    time = day[i] + i
    if time <= n:
        dp[i] = max(value[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)