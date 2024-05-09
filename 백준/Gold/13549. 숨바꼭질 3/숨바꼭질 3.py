import sys
from collections import deque

def bfs():
    while(q):
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        if x*2 <= 100000 and visited[x*2] == -1:
            visited[x*2] = visited[x]
            q.append(x*2)  # 2*x의 우선순위를 제일 높이기 위함이다.
        if x-1 >= 0 and visited[x-1] == -1:
            visited[x-1] = visited[x] + 1
            q.append(x-1)
        if x+1 <= 100000 and visited[x+1] == -1:
            visited[x+1] = visited[x]+1
            q.append(x+1)

n,k = map(int, sys.stdin.readline().split())
q = deque()
q.append(n)
visited=[-1 for _ in range(100001)]
visited[n]=0

bfs()