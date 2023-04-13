from collections import deque
def bfs(q):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while q:
        y, x=q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if( 0<=ny<N and 0<=nx<M and boolBox[ny][nx]==1):
                boolBox[ny][nx] = 0
                q.append((ny, nx))



T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    
    count =0
    boolBox = [ [0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        boolBox[y][x] = 1
    
    for i in range(M):
        for j in range(N):
            if(boolBox[j][i]==1):
                boolBox[j][i] = 0
                queue = deque([(j, i)])
                bfs(queue)
                count+=1
    print(count)

