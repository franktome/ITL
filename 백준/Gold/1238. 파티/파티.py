import sys
import heapq
input = sys.stdin.readline
inf = int(10e9)

n ,m, x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start,end):
    distance = [inf] * (n + 1)
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while(q):
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance[end]

costs=[]
for i in range(1,n+1):
    go = dijkstra(i,x)
    back = dijkstra(x,i)
    costs.append(go+back)
print(max(costs))