import sys
N = int(sys.stdin.readline())
ans=[]

for i in range(N):
    a = list(map(str, sys.stdin.readline().split()))
    
    if(a[0]=="push"):
        ans.append(int(a[1]))

    elif (a[0]=="pop"):
        if(len(ans)==0):
            print(-1)
        else:
            print(ans.pop())

    elif (a[0]=="size"):
        print(len(ans))
    
    elif(a[0]=="empty"):
        if(len(ans)==0):
            print(1)
        else:
            print(0)
    
    elif(a[0]=="top"):
        if(len(ans)==0):
            print(-1)
        else:
            print(ans[-1])
