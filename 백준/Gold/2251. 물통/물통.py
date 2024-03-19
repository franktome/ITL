import sys
from collections import deque

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x,y))

def bfs():
    while q:
        a1,b1 = q.pop()
        c1=c-a1-b1

        if a1==0:
            res.append(c1)

        # a>b
        water=min(a1,b-b1)
        pour(a1-water,b1+water)
        # b>a
        water = min(b1,a-a1)
        pour(a1+water,b1-water)
        # b>c
        water = min(b1, c-c1)
        pour(a1,b1-water)
        # c>b
        water = min(c1, b-b1)
        pour(a1, b1+water)
        # a>c
        water = min(a1,c-c1)
        pour(a1-water,b1)
        # c>a
        water=min(c1,a-a1)
        pour(a1+water,b1)

a,b,c = map(int, sys.stdin.readline().split())
q = deque()
q.append((0,0))

visited = [[False for _ in range(201)] for _ in range(201)]
visited[0][0] = True

res=[]
bfs()

res.sort()
for i in range(len(res)):
    print(res[i],end=' ')