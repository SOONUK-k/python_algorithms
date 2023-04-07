
from collections import deque


# 가로 m , 세로 n
dx = [-1, 1, 0, 0]
dy = [0 , 0, -1 ,1]
def bfs():
    while coin:
        x1, y1, x2, y2 , cnt = coin.popleft()
        if cnt >=10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

        ## 1.both inside
            if( 0<=nx1<M and 0<=ny1<N and 0<=nx2<M and 0<=ny2<N ):
                if(board[ny1][nx1] == "#"):
                    nx1, ny1 =x1, y1
                if(board[ny2][nx2] == "#"):
                    nx2, ny2 =x2, y2
                coin.append((nx1, ny1, nx2, ny2, cnt+1))
        ## 2. one outside
            elif(0<=nx1<M and 0<=ny1<N):
                return cnt+1
            elif(0<=nx2<M and 0<=ny2<N):
                return cnt+1
        ## 3. both outside
            else:
                continue
    return -1

if __name__ == "__main__":
    N, M = map(int, input().split())
    coin =deque()

    coin = deque()
    board = []
    temp = []
    for i in range(N):
        board.append(list(input().strip()))
        for j in range(M):
            if board[i][j] == "o":
                temp.append((i, j))



    coin.append((temp[0][1],temp[0][0] , temp[1][1], temp[1][0], 0))
    print(bfs())
        


