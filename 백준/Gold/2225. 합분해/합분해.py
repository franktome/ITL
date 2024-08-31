# <DP풀때 유의점>
# 점화식을 찾자(규칙성을 찾자)
# 보텀업으로 풀려고 해보자(표를 채우는 방식)

# k에 따라 출력값이 어떻게 달라지는 지 찾고 규칙성 발견하기
import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[1]*(n+1) for _ in range(k+1)]

for i in range(2,k+1):
    for j in range(1,n+1):
        if j==1:
            dp[i][j]=dp[i-1][j]+1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[k][n]%1000000000)