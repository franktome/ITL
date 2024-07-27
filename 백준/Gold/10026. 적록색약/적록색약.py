from collections import deque
import sys

n=int(sys.stdin.readline())
graph=[]
r_count=0
g_count=0
b_count=0
rg_count=0

for i in range(n):
    graph.append(list(sys.stdin.readline()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs_r(a,b):
    global r_count
    queue = deque([[a,b]])
    graph[a][b]="RG"
    while(queue):
        x,y=queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if graph[nx][ny]=="R":
                    graph[nx][ny] = "RG"
                    queue.append([nx,ny])
    r_count+=1

def bfs_g(a,b):
    global g_count
    queue = deque([[a,b]])
    graph[a][b] = "RG"
    while(queue):
        x,y=queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if graph[nx][ny]=="G":
                    graph[nx][ny] = "RG"
                    queue.append([nx,ny])
    g_count+=1

def bfs_b(a,b):
    global b_count
    queue = deque([[a,b]])
    while(queue):
        x,y=queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if graph[nx][ny]=="B":
                    graph[nx][ny] = " "
                    queue.append([nx,ny])
    b_count+=1

def bfs_rg(a,b):
    global rg_count
    queue = deque([[a,b]])
    while(queue):
        x,y=queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if graph[nx][ny]=="RG" :
                    graph[nx][ny] = " "
                    queue.append([nx,ny])
    rg_count+=1

for i in range(n):
    for j in range(n):
        if graph[i][j]=="R":
            bfs_r(i,j)
        elif graph[i][j] == "G":
            bfs_g(i, j)
        elif graph[i][j] == "B":
            bfs_b(i, j)


for i in range(n):
    for j in range(n):
        if graph[i][j]=="RG":
            bfs_rg(i,j)

print(r_count + g_count + b_count, rg_count+b_count)