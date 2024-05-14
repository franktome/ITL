import sys

n = int(sys.stdin.readline())
rec = [1001 for _ in range(n)]
rec[0]=0
lst = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    k = lst[i]
    for j in range(1, k+1):
        if (i+j < n):
            rec[i + j] = min(rec[i+j], rec[i]+1)

if rec[n-1]==1001:
    print(-1)
else:
    print(rec[n-1])