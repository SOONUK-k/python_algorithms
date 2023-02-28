n = int(input())
arr = range(1,n+1)

s=[]

def dfs():
    if len(s)==n:
        print(' '.join(map(str,s)))
        return
    
    for i in range(len(arr)):
        if arr[i] not in s:
            s.append(arr[i])
            dfs()
            s.pop()           
dfs()