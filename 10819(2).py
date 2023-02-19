N =int(input())
nums = sorted(list(map(int, input().split())))
bools =[0]*N
li=[]
ans=[]

def dfs():
    if len(li)==N:
        result =0

        for j in range(N-1):
            result += abs(li[j]-li[j+1])
        ans.append(result)
        return
    
    for i in range(N):
        if bools[i]:
            continue
        li.append(nums[i])
        bools[i]=1
        dfs()
        li.pop()
        bools[i]=0
dfs()

print(max(ans))


