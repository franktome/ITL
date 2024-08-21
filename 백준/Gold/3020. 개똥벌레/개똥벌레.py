import sys

n,h = map(int,sys.stdin.readline().split())

ground=[0] * (h+1)
cell = [0] * (h+1)

for i in range(n):
    size=int(sys.stdin.readline())
    if i%2==0:
        ground[size]+=1
    else:
        cell[size]+=1

for i in range(h-1,0,-1):
    ground[i]+=ground[i+1]
    cell[i]+=cell[i+1]

min_num=n
min_count=0
for i in range(1,h+1):
    if  min_num > ground[i]+cell[h-i+1]:
        min_num=ground[i]+cell[h-i+1]
        min_count=1
    elif min_num == ground[i]+cell[h-i+1]:
        min_count+=1

print(min_num, min_count)