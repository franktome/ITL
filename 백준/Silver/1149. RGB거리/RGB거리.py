import sys
n = int(sys.stdin.readline())

home=[]
home.append(list(map(int, sys.stdin.readline().split())))
for i in range(1,n):
    r, g, b = map(int, sys.stdin.readline().split())
    nhome=[]
    nhome.append(min(home[i-1][1], home[i-1][2]) + r)
    nhome.append(min(home[i-1][0], home[i-1][2]) + g)
    nhome.append(min(home[i - 1][0], home[i - 1][1]) + b)
    home.append(nhome)

print(min(home[n-1]))