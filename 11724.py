import sys
from collections import deque
input = sys.stdin.readline
def bfs(aq):
    while aq:
        currentI = aq.popleft()

        #미방문 상태
        if(bools[currentI] ==0):
            for j in range(N):
                if matrix[currentI][j]==1 and bools[j] == 0:
                    aq.append(j)
            bools[currentI]=1


N, M = map(int, input().split())
matrix =[[0]*N for _ in range(N)]
bools = [0 for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

count = 0
q= deque([])

#Logic
for i in range(N):
    if bools[i]==1:
        continue
    check = False
    for j in range(N):
        if( matrix[i][j]==1):
            check =True
            q.append(j)
    bools[i]=1
    if(check):
        count+=1
        bfs(q)    

for i in range(N):
    if bools[i]==0:
        count+=1

print(count)    
