import sys
from collections import deque

# 1. 인자 입력받기
n,m = map(int,sys.stdin.readline().split())
graph=[]
result = [[0]*m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

# 2. 0을 그룹으로 묶고 딕셔너리로 계산하기
group = {}

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a,b,index):
    queue=deque([[a,b]])
    graph[a][b] = index
    count=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m :
                if graph[nx][ny]==0:
                    graph[nx][ny]=index
                    queue.append([nx,ny])
                    count+=1
    group[index] = count

index=2
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            bfs(i,j,index)
            index+=1

# 3. 순서대로 돌면서 1을 기준으로 인접한 그룹들 찾은다음 그룹의 원소 갯수 찾기

for i in range(n):
    for j in range(m):
        linked = []
        count=0
        if graph[i][j]==1:
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0<=x<n and 0<=y<m and graph[x][y]!=1:
                    linked.append(graph[x][y])
            linked=list(set(linked))
            for k in range(len(linked)):
                count+=group[linked[k]]
            result[i][j]=(count+1)%10


# 4. 그래프에 업데이트 하고 출력하기
for i in range(n):
    for j in range(m):
        print(result[i][j],end='')
    print()