N = int(input())
ans = list(map(int, input().split()))
ansStr = ' '.join(map(str, ans))
check= 0
nums = range(1, N+1)
bools= [0]*N
li=[]

def dfs():
    global check
    if len(li)==N:
        s=' '.join(map(str,li))
        if (check==1):
            print(s)
            check+=1
        if s == ansStr:
            check+=1
        return
    for i in range(N):
        if bools[i] or check==2:
            continue
        li.append(nums[i])
        bools[i] = 1
        dfs()
        li.pop()
        bools[i] = 0

dfs()
if(check !=2):
    print(-1)
