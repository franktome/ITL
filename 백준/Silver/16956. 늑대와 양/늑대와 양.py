import sys
r,c=map(int,sys.stdin.readline().split())
lst=[]
result=1
for i in range(r):
    lst.append(sys.stdin.readline())

for i in range(r):
    for j in range(c):
        if lst[i][j]=='S':
            if lst[i][j-1]=='W' if j-1>=0 else False:
                result=0
            if lst[i][j+1]=='W' if j+1 < c else False:
                result=0
            if lst[i-1][j]=='W' if i-1>=0 else False:
                result=0
            if lst[i+1][j]=='W' if i+1<r else False:
                result=0
print(result)
if result==1:
    for i in range(r):
        print(lst[i].replace('.','D'),end='')