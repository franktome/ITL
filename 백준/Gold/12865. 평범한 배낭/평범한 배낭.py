import sys

n, k = map(int,sys.stdin.readline().split())
bag=[[0,0]]
for i in range(n):
    bag.append(list(map(int, sys.stdin.readline().split())))
dp = [[0]*(k+1) for _ in range(n+1)]
# d[n][k]는 N번째 물건 까지 살펴보았을 때, 무게가 K인 배낭의 최대 가치 이다.
# 첫번째 index는 물건의 순번, 두번재 index는 물건의 가치이다.

for i in range(1,n+1):
    for j in range(1,k+1):
        v = bag[i][1] #  i번째 물건의 가치
        w = bag[i][0] #  i번째 물건의 무게
        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])