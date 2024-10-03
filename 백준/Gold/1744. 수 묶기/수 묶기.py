import sys
input=sys.stdin.readline
n = int(input().strip())
arr=[int(input().strip()) for _ in range(n)]

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
    elif arr[i]==0: # zero flag : 만약 음수가 나오면 음수를 없앨 수 있다.
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
        else: # 만약 zero가 1이라면 0이 있다는 뜻이므로 마지막 항은 안 더해도 된다.
            continue
print(sum)