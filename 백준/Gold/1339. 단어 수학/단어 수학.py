import sys

n= int(sys.stdin.readline())
words=[sys.stdin.readline().strip() for _ in range(n)]

dic={}
for word in words:
    x=len(word)-1
    for j in word:
        if j in dic:
            dic[j]+=10**x
        else:
            dic[j]=10**x
        x-=1

dic2 = sorted(dic.values(),reverse=True)

k=9
sum=0
for i in dic2:
    sum+=i*k
    k-=1
print(sum)