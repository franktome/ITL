# 스크린 상태, 클립보드 상태, 횟수 관리해주기
import sys
from collections import deque

def bfs():
    while(q):
        s, c = q.popleft()
        if s==n:
            print(visited[s][c])
            break

        if visited[s][s] == -1:
            visited[s][s] = visited[s][c] + 1
            q.append((s,s))
        if s+c<=n and visited[s+c][c]==-1:
            visited[s+c][c] = visited[s][c] + 1
            q.append((s+c,c))
        if s-1>=0 and visited[s-1][c]==-1:
            visited[s-1][c]=visited[s][c]+1
            q.append((s-1,c))

n=int(sys.stdin.readline())
# 화면의 이모티콘의 갯수, 클립보드 이모티콘의 갯수
q=deque()
q.append((1,0))
visited=[[-1]*(n+1) for _ in range(n+1)]
visited[1][0]=0

bfs()