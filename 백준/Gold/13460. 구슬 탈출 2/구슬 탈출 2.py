import sys
input = sys.stdin.readline

def move(x,y,d):
    cnt=0
    back = 0
    nx,ny = x,y
    while(1):
        cnt+=1
        nx, ny = nx+dx[d], ny+dy[d]
        if graph[nx][ny]=='R' or graph[nx][ny]=='B':
            back=-1
        if graph[nx][ny]=='#':
            return cnt+back-1
        if graph[nx][ny]=='O':
            return cnt

def dfs(ri,rj,bi,bj,depth):
    global ans
    if depth>10:
        return
    for i in range(4):
        rmove = move(ri, rj, i)
        bmove = move(bi, bj, i)
        if rmove==0 and bmove==0:
            continue
        nri, nrj = ri+dx[i]*rmove,rj+dy[i]*rmove

        nbi, nbj = bi+dx[i]*bmove,bj+dy[i]*bmove

        if graph[nbi][nbj]=='O':
            continue # fail
        else:
            if graph[nri][nrj]=='O':
                ans = min(ans,depth)  # 성공한 경우
                return
        graph[ri][rj], graph[bi][bj] = '.', '.'
        graph[nri][nrj], graph[nbi][nbj] = 'R', 'B'
        dfs(nri, nrj, nbi, nbj, depth + 1)
        graph[nri][nrj], graph[nbi][nbj] = '.', '.'
        graph[ri][rj], graph[bi][bj] = 'R', 'B'


n,m = map(int, input().split())
graph=[list(input().strip()) for _ in range(n)]
ri,rj,bi,bj=0,0,0,0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(n):
    for j in range(m):
        if graph[i][j]=='R':
            ri,rj = i,j
        elif graph[i][j]=='B':
            bi,bj = i,j
ans=11

dfs(ri,rj,bi,bj,1)

if ans==11:
    print(-1)
else:
    print(ans)