import sys
k = int(sys.stdin.readline())

ans=[]
for i in range(k):
    n = int(sys.stdin.readline())
    if(n==0):
        ans.pop()
    else:
        ans.append(n)

print(sum(ans))