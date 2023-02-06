N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
ans=[]
def dfs(a):
    if len(ans)==M:
        print(' '.join(map(str, ans)))
        return
    for i in range(a, len(numList)):
        ans.append(numList[i])
        dfs(i)
        ans.pop()

dfs(0)

