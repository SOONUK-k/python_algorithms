n = int(input())
arr = list(map(int, input().split()))

x,y = 0,0
a = True
for i in range(n-1,0,-1):
    if arr[i]>arr[i-1]:
        x, y = i-1, i
        for j in range(n-1,0,-1):
            if arr[j]>arr[x]:
                arr[j], arr[x] = arr[x], arr[j]
                a= False
                break
    if a==False:
        arr= arr[:y] + sorted(arr[y:])
        print(*arr)
        break
if a==True:
    print(-1)