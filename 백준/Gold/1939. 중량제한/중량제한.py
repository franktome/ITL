import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
start, end = map(int, sys.stdin.readline().split())

def bfs(s,e,w):
    visited=[0 for _ in range(n+1)]
    visited[s]=1
    q=deque([s])
    while q:
        a = q.popleft()
        if a==end:
            return True
        for i in graph[a]:
            if visited[i[0]]==0 and i[1]>=w:
                visited[i[0]]=1
                q.append(i[0])


low = 1
high = 1000000000
res=0

while low<=high:
    mid=(low+high)//2
    if bfs(start, end, mid):
        res=mid
        low = mid+1
    else :
        high = mid-1
print(res)