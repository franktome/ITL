import heapq

n = int(input())
lst = []
for _ in range(n):
    tmp = int(input())
    heapq.heappush(lst, tmp)

ans = 0
while (len(lst)>1):
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    ans += a+b
    heapq.heappush(lst, a+b)

print(ans)