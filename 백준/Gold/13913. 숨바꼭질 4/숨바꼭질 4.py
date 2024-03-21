import sys
from collections import deque

def move(a, b):
    if b>=0 and b<=100000:
        if visited[b]==0:
            visited[b] = visited[a]+1
            q.append(b)
            traj[b] = a
def bfs():
    while q:
        x = q.popleft()
        if x==k:
            print(visited[x])
            temp=x
            arr=[]
            for _ in range(visited[x]+1):
                arr.append(temp)
                temp=traj[temp]
            print(' '.join(map(str,arr[::-1])))
            break
        move(x, x - 1)
        move(x, x + 1)
        move(x, x * 2)

n,k = map(int, sys.stdin.readline().split())

q = deque()
q.append(n)

visited = [0 for _ in range(100001)]
traj = [0 for _ in range(100001)]

bfs()