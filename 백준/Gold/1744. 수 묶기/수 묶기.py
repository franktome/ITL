# 1. 입력을 받는다.
# 2. 양수는 내림차순으로 정렬하여 2개씩 묶는다.
# 3. 음수도 내림차순으로 정렬하여 2개씩 묶는다.
# 3. 0은 음수가 있으면 없애고 없다면 그냥 무시
# 4. 1은 무조건 더한다.

import sys
n = int(sys.stdin.readline().strip())
arr=[int(sys.stdin.readline().strip()) for _ in range(n)]

plus=[]
minus=[]
zero=0
sum=0

for i in range(n):
    if arr[i] == 1:
        sum+=1
    elif arr[i]>0 :
        plus.append(arr[i])
    elif arr[i]<0:
        minus.append(arr[i])
    elif arr[i]==0:
        zero=1

plus.sort(reverse=True)
minus.sort()

for i in range(0,len(plus),2):
    if i+1<len(plus):
        sum+=plus[i]*plus[i+1]
    else :
        sum+=plus[i]

for i in range(0,len(minus),2):
    if i+1<len(minus):
        sum+=minus[i]*minus[i+1]
    else :
        if zero==0:
            sum += minus[i]

print(sum)