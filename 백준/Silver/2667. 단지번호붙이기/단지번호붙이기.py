import sys
from collections import deque

n = int(sys.stdin.readline())
graph=[]
queue=deque()
res=[]

for i in range(n):
    graph.append(list(map(int,list(sys.stdin.readline().strip()))))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(a,b):
    graph[a][b]=0   # 이부분이 중요하구나
    queue.append([a,b])
    count=1
    while(queue):
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if graph[nx][ny]==1:
                    graph[nx][ny]=0
                    count+=1
                    queue.append([nx,ny])
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            res.append(bfs(i,j))
res=sorted(res)
print(len(res))
for i in range(len(res)):
    print(res[i])