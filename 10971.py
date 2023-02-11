

ans=[]
N = int(input())

array = [list(map(int, input().split())) for _ in range(N)]

arr = range(N)
nPr=[]
s=[]
def dfs():
    if len(s)==N:
        news =[]
        for j in s:
            news.append(j)
        nPr.append(news)
        return
    
    for i in range(len(arr)):
        if arr[i] not in s:
            s.append(arr[i])
            dfs()
            s.pop()           

dfs()


for i in range(len(nPr)):
    distance=0
    position = nPr[i][-1]
    for j in range(N):
        willposition=nPr[i][j]
        if (array[position][willposition] == 0):
            distance=0
            break
        else:
            distance += array[position][willposition]
            position = willposition
    if distance !=0:
        ans.append(distance)

print(min(ans))
