N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
ans=[]
def dfs():
    if len(ans)==M:
        print(' '.join(map(str, ans)))
        return
    for i in range(len(numList)):
        ans.append(numList[i])
        dfs()
        ans.pop()

dfs()