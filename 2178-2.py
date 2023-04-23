from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]

def bfs(start):
    queue = deque([start])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1
                queue.append((ny, nx))

    return maze[N-1][M-1]

print(bfs((0, 0)))