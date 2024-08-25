import sys

n, k = map(int,sys.stdin.readline().split())
bag = [list(map(int,sys.stdin.readline().split()) )for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):   # n은 물건을 꺼내기 위한 인덱스
    for j in range(1,k+1):  # k는 dp table을 관리하기 위한 인덱스
        if j>= bag[i-1][0]:  # 0은 무게, 1은 가치
            dp[i][j] = max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])