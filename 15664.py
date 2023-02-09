N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
d = {}; li = []
bools= [0]*N

def dfs(a):
    if len(li)==M:
        s = ' '.join(map(str,li))
        if s not in d:
            d[s] =1
            print(s)
        return
    for i in range(a,N):
        li.append(nums[i])
        dfs(i+1)
        li.pop()
dfs(0)
