N, M = list(map(int, input().split()))


ans=[]
def dfs(a):
    if len(ans)==M:
        print(*ans)
        return
    else:
        for i in range(a,N+1):
            ans.append(i)
            dfs(i)
            ans.pop()

dfs(1)