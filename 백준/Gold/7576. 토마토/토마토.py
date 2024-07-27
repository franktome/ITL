import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())
graph=[]
queue=deque()
res=0

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx=[0,0,-1,1]
dy=[-1,1,0,0]

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append([i,j])

def bfs():
    while(queue):
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx>=0 and nx<n and ny>=0 and ny<m:
                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1
                    queue.append([nx,ny])

bfs()
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            print(-1)
            exit(0)
        res=max(res,graph[i][j])

print(res-1)