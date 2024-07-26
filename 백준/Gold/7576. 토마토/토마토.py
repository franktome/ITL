import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
queue1 = deque()
queue2 = deque()
record=[[0 for _ in range(m)] for _ in range(n)]
before_ripe=0
after_ripe=0
final_date=0
not_able=0


graph=[]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):                  # 초기에 토마토의 위치 알아내기
    for j in range(m):
        if graph[i][j]==1 :
            queue1.append([i, j])
        elif graph[i][j]==0:
            before_ripe=1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while(1):
        if len(queue1)==0 and len(queue2)==0:
            break

        while (queue1):
            x, y = queue1.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        record[nx][ny] = record[x][y] + 1
                        queue2.append([nx, ny])

        while (queue2):
            x, y = queue2.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        record[nx][ny] = record[x][y] + 1
                        queue1.append([nx, ny])

bfs()

if before_ripe==0 :
    print(0)
else :
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                print(-1)
                after_ripe=1
                break
        if after_ripe==1:
            break
    if after_ripe==0:
        for i in range(n):
            for j in range(m):
                if record[i][j]>final_date:
                    final_date=record[i][j]
        print(final_date)
