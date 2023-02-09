N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

li=[]
d={}

def dfs():
    if len(li)==M:
        s = ' '.join(map(str,li))
        if s not in d:
            d[s]=1
            print(s)
        return
    
    for i in range(N):
        li.append(nums[i])
        dfs()
        li.pop()

dfs()