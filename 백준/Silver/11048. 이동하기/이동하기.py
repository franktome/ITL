import sys

n,m = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(m)] for _ in range(n)]

candy = []
for _ in range(n):
    candy.append(list(map(int, sys.stdin.readline().split())))

dp[0][0] = candy[0][0]

for i in range(n):
    for j in range(m):
        if i+1 < n and j+1 < m:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+candy[i+1][j+1])
        if j+1<m:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j]+candy[i][j+1])
        if i+1<n:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+candy[i+1][j])
print(dp[n-1][m-1])