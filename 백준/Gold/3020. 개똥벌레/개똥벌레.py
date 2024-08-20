import sys

n, h = map(int, sys.stdin.readline().split())
ground=[]
sky=[]
for i in range(n):
    if i%2==0:
        ground.append(int(sys.stdin.readline().strip()))
    else:
        sky.append(int(sys.stdin.readline().strip()))

sky.sort()
ground.sort()
ans=0; count=0

res=[]
for i in range(1,h+1):
    # 석순 이진탐색
    count = 0
    start1 = 0
    end1 = len(ground)-1
    res1 = len(ground)
    while (start1<=end1):
        mid = (start1 + end1) // 2
        if ground[mid] >= i:
            res1 = mid
            end1 =mid-1
        else :
            start1 = mid+1
    count+=(len(ground)-res1)

    # 종유석 이진탐색
    start2=0
    end2=len(sky)-1
    res2=len(sky)
    while (start2<=end2):
        mid =(start2+end2)//2
        if h-sky[mid]<i:
            res2=mid
            end2 = mid - 1
        else:
            start2 = mid + 1
    count+=(len(sky)-res2)
    res.append(count)

k=min(res)
print(k, res.count(k))