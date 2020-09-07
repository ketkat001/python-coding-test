T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    temp_list = list(map(int, input().split()))
    miner_list = [[] for _ in range(n)]
    for i in range(n):
        miner_list[i] = temp_list[i*m:i*m+m]
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] = miner_list[i][0]
    for j in range(1, m):
        dp[0][j] = max(dp[0][j-1], dp[1][j-1]) + miner_list[0][j]
        for i in range(1, n-1):
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + miner_list[i][j]
        dp[n-1][j] = max(dp[n-2][j-1], dp[n-1][j-1]) + miner_list[n-1][j]
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)