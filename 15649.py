
N, M = list(map(int,input().split()))

ans =[]
bools = [0 for _ in range(N)]

def dfs():
    if len(ans)==M:
        print(*ans)
        return
    
    for i in range(1, N+1):
        if not bools[i-1]:
            ans.append(i)
            bools[i-1] = 1
            dfs()
            ans.pop()
            bools[i-1] = 0
    
dfs()
























# n,m = list(map(int,input().split()))
 
# s = []
 
# def dfs():
#     if len(s)==m:
#         print(' '.join(map(str,s)))
#         return
    
#     for i in range(1,n+1):
#         if i not in s:
#             s.append(i)
#             dfs()
#             s.pop()
 
# dfs()