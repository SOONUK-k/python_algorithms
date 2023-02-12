


while(True):

    inputs = list(map(int, input().split()))
    if(inputs[0]==0):
        break
    li=[]
    #값 세팅
    arr=[]
    bools = [0]*inputs[0]

    for i in range(1,len(inputs)):
        arr.append(inputs[i])

    def dfs(a):
        if len(li)==6:
            print(*li)
            return

        for i in range(a, inputs[0] ):
            if bools[i]:
                continue
            li.append(arr[i])
            bools[i] = 1
            dfs(i)
            li.pop()
            bools[i] = 0

    dfs(0)
    print()

