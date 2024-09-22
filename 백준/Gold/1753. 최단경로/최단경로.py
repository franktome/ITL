import sys
import heapq
input=sys.stdin.readline
inf = int(10e9)

v,e = map(int, input().split())
start = int(input())

graph=[[] for _ in range(v+1)]
distance=[inf for _ in range(v+1)]
distance[start]=0

for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

q=[]
heapq.heappush(q,(0,start))

while(q):
    d, n = heapq.heappop(q)

    if distance[n]<d:
        continue

    for i in graph[n]:
        cost = d + i[1]
        if cost<distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))


for i in range(1,v+1):
    if distance[i]==inf:
        print("INF")
    else:
        print(distance[i])