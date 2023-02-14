
N = int(input())
nums = sorted(map(int, input().split()))
ans=[]; li = []
bools= [0]*N

#cl = currentList
#bs = booleans

def dfs(bs, cl):
    if len(cl) == N:
        s = ' '.join(map(str, cl))
        print(s)

    for i in range(N):
        if not bools[i]:
            bs[i] = 1
            #
            newcl=[]
            for i in cl:
                newcl.append(i)
            newcl.append(nums[i])
            #
            dfs(bs, newcl)
            bs[i] =0

dfs(bools, li)