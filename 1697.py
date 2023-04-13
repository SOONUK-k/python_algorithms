from collections import deque
N, K = map(int, input().split())
check = [0 for _ in range(100001)]

def bfs(start):
    queue = deque([start])
    dx = [-1, 1]
    check[start] =1
    while check[K] ==0:
        n = queue.popleft()

        # +1, -1 moving
        for i in range(2):
            ny = n + dx[i]
            if 0 <= ny <= 100000 and check[ny] == 0:  # Check bounds and visit status
                check[ny] = check[n] + 1
                queue.append(ny)
        
        # *2 moving
        ny = n * 2
        if 0 <= ny <= 100000 and check[ny] == 0:  # Check bounds and visit status
            check[ny] = check[n] + 1
            queue.append(ny)
    return check[K]-1

print(bfs(N))