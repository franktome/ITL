import sys

n = int(sys.stdin.readline())

time=[]
count=0
start=0
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    time.append([a,b])

time.sort(key=lambda x:(x[1],x[0]))

for i in range(n):
    if time[i][0]>=start:
        count+=1
        start=time[i][1]

print(count)