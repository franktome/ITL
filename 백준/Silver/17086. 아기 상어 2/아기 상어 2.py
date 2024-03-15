import sys
import queue
lst=[]

n,m = map(int, sys.stdin.readline().split())
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

queue = queue.Queue()
for i in range(n):
    for j in range(m):
        if lst[i][j]==1:
            queue.put([i,j])

while(not queue.empty()) :
    dx = [0,0,-1,1,1,1,-1,-1]
    dy = [-1,1,0,0,1,-1,1,-1]
    x,y = queue.get()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx>=0 and nx<n) and (ny>=0 and ny<m):
            if lst[nx][ny]==0:
                lst[nx][ny] = lst[x][y]+1
                queue.put([nx,ny])
print(max(map(max,lst))-1)