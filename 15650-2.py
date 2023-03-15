N, M = list(map(int, input().split()))

ans =[]
bools =[]
def dfs(start):
    if len(ans)==M:
        print(*ans)
        return
    
    for i in range(start,N+1):
        ans.append(i)
        dfs(i+1)
        ans.pop()
dfs(1)