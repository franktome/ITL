import sys

# 1. 인자들 입력받기
n=int(sys.stdin.readline())
a,b = map(int,sys.stdin.readline().split())
r=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)] # linked list로 구현할 때는 이렇게 구현해야 되는구나!!
visited = [0]*(n+1)
for _ in range(r):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. dfs로 돌면서 b에 도달할 때가지 거리 계산하기
def dfs(node):
    for x in graph[node]:
        if visited[x]==0:
            visited[x]=visited[node]+1
            if x==b:
                break
            else:
                dfs(x)

# 3. 결과 출력하기
dfs(a)
if visited[b]==0:
    print(-1)
else:
    print(visited[b])