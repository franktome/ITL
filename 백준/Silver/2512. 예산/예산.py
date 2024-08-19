import sys

n= int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
s= int(sys.stdin.readline())

start, end= 1, max(arr)

while start <= end:
    mid = (start+end)//2
    sum=0
    for i in arr:
        sum+=min(i,mid)
    if sum<=s:  # 여기 범위를 조심해야겠다. 이하인지 미만인지 조심하기
        result=mid
        start = mid+1
    else:
        end = mid-1
print(result)