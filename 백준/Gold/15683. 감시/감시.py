import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [[6]*(m+2)] + [[6]+list(map(int,input().split()))+[6] for _ in range(n)] + [[6]*(m+2)]

lst=[]
for i in range(1,n+1):
    for j in range(1,m+1):
        if 1<=arr[i][j]<=5:
            lst.append((i,j)) # cctv의 위치 저장


cnt = len(lst)
ans=m*n

di=[-1,0,1,0]
dj=[0,1,0,-1]
cctv=[[],[1],[1,3],[0,1],[0,1,3],[0,1,2,3]]

def cal(tlst):  # 마지막에 최종적으로 각 cctv의 방향이 정해졌을 때 사각지대 계산하는 부분
    v = [[0] * (m + 2) for _ in range(n + 2)]

    for i in range(len(lst)):
        si, sj = lst[i]
        rot = tlst[i]
        type = arr[si][sj]

        for dr in cctv[type]:
            dr = (rot+dr) % 4
            ci,cj =si, sj  # 이부분 왜 이렇게 해줘야 하는지 잘 모르겠음
            while True:
                ci, cj = ci + di[dr], cj + dj[dr]
                if arr[ci][cj] == 6:
                    break
                v[ci][cj]=1
    cnt=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if v[i][j]==0 and arr[i][j]==0:
                cnt+=1
    return cnt

def dfs(num,tlst):   # tlst는 해당 횟수에 해당하는 cctv의 회전방향
    global ans
    if num==cnt:
        ans = min(ans, cal(tlst))
        return
    dfs(num + 1, tlst + [0])  # 0도 회전
    dfs(num + 1, tlst + [1])  # 90도 회전
    dfs(num + 1, tlst + [2])  # 180도 회전
    dfs(num + 1, tlst + [3])  # 270도 회전



dfs(0,[])
print(ans)