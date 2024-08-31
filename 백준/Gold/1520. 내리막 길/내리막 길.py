# <DP풀때 유의점>
# 점화식을 찾자(규칙성을 찾자)
# 보텀업으로 풀려고 해보자(표를 채우는 방식)

# top-down 방식으로 풀이한 것
import sys

m, n = map(int, sys.stdin.readline().split())
arr=[[0]*(n+2)]+[([0]+list(map(int,sys.stdin.readline().split()))+[0]) for _ in range(m)] + [[0]*(n+2)]
dp=[[-1]*(n+2) for _ in range(m+2)]
dp[1][1] = 1

def dfs(cx,cy):
    if dp[cx][cy]==-1:
        dp[cx][cy]=0
        for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
            px,py=cx+dx,cy+dy
            if arr[cx][cy]<arr[px][py]:
                dp[cx][cy]+=dfs(px,py)
    return dp[cx][cy]

print(dfs(m,n))