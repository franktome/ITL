import sys

plus=0
minus=0
num=""
flag=0  # flag 0은 플러스 1은 마이너스
str = sys.stdin.readline()

for i in range(len(str)):
    if str[i]>='0' and str[i]<='9':
        num+=str[i]
    else:
        if flag==0:
            plus+=int(num)
            num=""
        elif flag==1:
            minus+=int(num)
            num=""

        if str[i]=='-':
            flag=1

print(plus-minus)