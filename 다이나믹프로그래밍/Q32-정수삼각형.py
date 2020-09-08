n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*i for i in range(1, n+1)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i-1][j-1]
        if j == i:
            right_up = 0
        else:
            right_up = dp[i-1][j]
        dp[i][j] = triangle[i][j] + max(left_up, right_up)

print(max(dp[n-1]))