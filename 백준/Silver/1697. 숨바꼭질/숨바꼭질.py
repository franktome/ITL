import sys
from collections import deque

def move(a, b):
    if b>=0 and b<=100000:
        if visited[b]==0:
            visited[b] = visited[a]+1
            q.append(b)
def bfs():
    while q:
        x = q.popleft()
        if x==k:
            print(visited[x])
            break
        move(x, x - 1)
        move(x, x + 1)
        move(x, x * 2)

n,k = map(int, sys.stdin.readline().split())

q = deque()
q.append(n)

visited = [0 for _ in range(100001)]

bfs()