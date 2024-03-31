import sys
dict={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
sum=0
count=0
for i in range(20):
    _,a,b=sys.stdin.readline().split()
    if b!="P":
        a = int(a[0])
        count += a
        sum += a * dict[b]

print(sum/count)