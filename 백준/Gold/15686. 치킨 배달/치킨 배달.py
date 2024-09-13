# 치킨집 중 m개 남기기
# 가능한 모든 경우 2^13 < 2^50

import sys
input=sys.stdin.readline

N,M = map(int,input().split())
arr=[list(map(int, input().split())) for _ in range(N)]

def cal(tlst):
    # 모든 집과 tlst의 치킨집거리중 최소값의 누적합 구하기
    sm=0
    for hi,hj in home:
        mn=2*N
        for ci, cj in tlst:
            mn = min(mn, abs(hi-ci)+abs(hj-cj))
        sm+=mn
    return sm

def dfs(n, tlst):
    global ans
    if n==CNT:
        if len(tlst)==M:
            ans = min(ans, cal(tlst))
        return
    dfs(n+1, tlst+[chicken[n]])# 유지하는 경우
    dfs(n+1, tlst) # 폐업하는 경우




# 집, 치킨집의 좌표를 home, chicken[]에 저장
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] ==1:
            home.append((i,j))
        elif arr[i][j]==2:
            chicken.append((i,j))
CNT=len(chicken)
ans = 2*N*N*2 # 최대 2n개의 집이 가장 멀리 떨어진 치킨집과의 거리의 합

dfs(0,[])
print(ans)