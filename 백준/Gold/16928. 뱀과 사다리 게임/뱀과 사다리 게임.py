import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
ladder = {}
snake = {}

for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    ladder[x]=y   # 인덱스 조정

for i in range(m):
    x,y = map(int, sys.stdin.readline().split())
    snake[x]=y

grape = [-1 for _ in range(101)]
grape[1]=0
queue=deque([1])

def bfs():
    while queue:
        x = queue.popleft()
        for dx in range(1, 7):
            nx = x + dx
            if nx <= 100:
                if nx in ladder:
                    nx = ladder[nx]
                elif nx in snake:
                    nx = snake[nx]

                if grape[nx] == -1:
                    grape[nx] = grape[x] + 1
                    queue.append(nx)
                    if nx == 100:
                        return

bfs()
print(grape[100])