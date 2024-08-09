import sys

n=int(sys.stdin.readline())
words=[sys.stdin.readline().strip() for _ in range(n)]

dic = {}
for word in words:
    x=len(word)-1
    for i in word:
        if i in dic:
            dic[i] += 10 ** x
        else:
            dic[i]= 10 ** x
        x-=1
dic1=sorted(dic.values(),reverse=True)
k=9
sum=0
for i in dic1:
    sum += i*k
    k-=1
print(sum)