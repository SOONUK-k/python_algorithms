
N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
d = {}; li = []
bools= [0]*N

def dfs():
    if len(li)==M:
        s = ' '.join(map(str,li))
        if s not in d:
            d[s] =1
            print(s)
        return
    for i in range(N):
        if bools[i]:
            continue
        li.append(nums[i])
        bools[i] = 1
        dfs()
        li.pop()
        bools[i] = 0
dfs()
