import sys
n=int(sys.stdin.readline().rstrip())
count=n
for i in range(n):
    word=sys.stdin.readline().rstrip()
    for j in range(len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count-=1
            break
print(count)