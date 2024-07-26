from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
queue=deque()
visited=[False for _ in range(n+1)]
count=0

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue.append(start)
    visited[start]=True
    while(queue):
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        count+=1

print(count)