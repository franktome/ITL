import sys

n = int(sys.stdin.readline())

dp=[0]*(32)

dp[2] = 3

for i in range(4, n+1, 2):
    dp[i] = dp[i-2]*3 + sum(dp[:i-2])*2+2

print(dp[n])