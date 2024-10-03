import sys
input = sys.stdin.readline

# 로테이션 방향과 cctv type 정의
dx=[-1,0,1,0]
dy=[0,1,0,-1]
cctv=[[],[1],[1,3],[0,1],[0,1,3],[0,1,2,3]]

def cal(tlst):
    # 이 부분을 간과했네!! visited를 따로 관리하자!!
    v = [[0]*(m+2) for _ in range(n+2)]

    for i in range(cnt):
        x,y = lst[i]
        rot = tlst[i]
        type = graph[x][y]

        for d in cctv[type]:
            dr = (d+rot)%4
            cx,cy = x,y
            while(True):
                cx, cy = cx + dx[dr], cy + dy[dr]
                if graph[cx][cy]==6:
                    break
                v[cx][cy] = 1

    count=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if v[i][j]==0 and graph[i][j]==0:
                count+=1
    return count


def dfs(n,tlst):
    global ans
    if n==cnt:
        ans = min(ans, cal(tlst))
        return
    dfs(n + 1, tlst + [0])
    dfs(n + 1, tlst + [1])
    dfs(n + 1, tlst + [2])
    dfs(n + 1, tlst + [3])



lst=[]
tlst=[]
n,m = map(int,input().split())
graph=[[6]*(m+2)] + [([6]+list(map(int,input().split()))+[6]) for _ in range(n)] + [[6]*(m+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if 1<=graph[i][j]<=5:
            lst.append((i,j)) # cctv 따로 저장
cnt = len(lst)
ans = n*m


dfs(0,[])
print(ans)