import sys
from collections import deque

dx=[-1,0,1,-1,1,-1,0,1]
dy=[1,1,1,0,0,-1,-1,-1]

# 1. bfs 정의해서 각 맵에서 섬의 갯수 구하기
def bfs(a, b):
    queue = deque([[a, b]])
    graph[a][b] = 0
    while (queue):
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append([nx, ny])

# 2. 무한반복문 안에서 인자 입력받기 -> 만약 0 0 이면 반복문 종료시키기
result=[]
while(True):
    count=0

    w,h=map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    graph=[]
    for i in range(h):
        graph.append(list(map(int,sys.stdin.readline().split())))
    # 3. 섬의 갯수 리스트에서 append하기
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                bfs(i,j)
                count+=1
    result.append(count)


# 4. 반복문 돌면서 섬의 갯수 출력하기
for i in range(len(result)):
    print(result[i])