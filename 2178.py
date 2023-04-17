N, M = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]
bool_maze = [[0 for _ in range(M)] for _ in range(N)]

output = (N * M)+1

def inbound(y,x):
    if(0<=y<N and 0<=x<M):
        return True
    return False

def dfs(n,m,count):
    global output

    if (n==N-1 and m==M-1):
        if(count<output):
            output = count
        return

    
    #Four direction moving
    #좌우, 우, 아래, 위 순서
    #방문하지않았고 범위 내에 있을때 방문이 가능함
    if( inbound(n, m-1) and bool_maze[n][m-1]==0):
        if( maze[n][m-1]==1):
            bool_maze[n][m-1] = 1
            dfs(n, m-1, count+1)
            bool_maze[n][m-1] = 0

    if( inbound(n, m+1) and bool_maze[n][m+1]==0 ):
        if(maze[n][m+1]==1):
            bool_maze[n][m+1] = 1
            dfs(n, m+1, count+1)
            bool_maze[n][m+1] = 0

    if( inbound(n-1, m) and bool_maze[n-1][m]==0 ):
        if(maze[n-1][m]==1):
            bool_maze[n-1][m] = 1
            dfs(n-1, m, count+1)
            bool_maze[n-1][m] = 0

    if( inbound(n+1, m) and bool_maze[n+1][m]==0):
        if(maze[n+1][m]==1):
            bool_maze[n+1][m] = 1
            dfs(n+1, m, count+1)
            bool_maze[n+1][m] = 0

bool_maze[0][0] = 1
dfs(0,0,1)
print(output)