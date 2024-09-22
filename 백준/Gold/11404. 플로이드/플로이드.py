import sys
input = sys.stdin.readline
inf = int(10e9)

n = int(input())
m = int(input())
graph=[[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = min(graph[a][b],c)  # 같은 노드를 잇는 여러개의 간선이 있을 수 있다.

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            graph[i][j]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==inf:
            print(0,end=" ")
        else:
            print(graph[i][j], end=" ")
    print()