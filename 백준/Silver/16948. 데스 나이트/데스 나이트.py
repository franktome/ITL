import sys
from collections import deque

n = int(sys.stdin.readline())
r1,c1,r2,c2 = map(int, sys.stdin.readline().split())

grape=[[-1 for _ in range(n)] for _ in range(n)]
grape[r1][c1]=0

queue =deque([[r1,c1]])

dx=[-2,-2,0,0,2,2]
dy=[-1,1,-2,2,-1,1]

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if grape[nx][ny] == -1:
                    grape[nx][ny] = grape[x][y] + 1
                    if nx==r2 and ny==c2:
                        return
                    queue.append([nx,ny])

bfs()

if grape[r2][c2] == -1:
    print(-1)
else :
    print(grape[r2][c2])