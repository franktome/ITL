import sys
from collections import deque

# 1. 변수들 입력받기
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
r = int(sys.stdin.readline())

# 2. 그래프 생성하기(linked list)
graph=[[-1 for _ in range(n+1)] for _ in range(n+1)]
graph[a][a]=0

for i in range(r):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 0
    graph[y][x] = 0

# 3. 시작점 입력받아서 그 점으로부터 bfs 돌리기(기존 그래프에다가 업데이트)
def bfs(x):
    queue = deque([[x,x]])
    while(queue):
        x1, y1 = queue.popleft()
        if y1==b:
            break
        for i in range(1, n+1):
            if x1 !=i and graph[y1][i]==0:
                graph[y1][i] = graph[x1][y1] + 1
                graph[i][y1] = graph[x1][y1] + 1
                queue.append([y1,i])


# 4. 결과 출력하기
bfs(a)

mx=0
for i in range(1,n+1):
    if graph[b][i]>0:
        mx=max(mx, graph[b][i])
if mx==0:
    print(-1)
else:
    print(mx)