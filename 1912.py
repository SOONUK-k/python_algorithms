
N = int(input())
arr = list(map(int, input().split()))

dp = [ 0 for  _ in range(N)]

for i in range(1,N):
    if(arr[i] < arr[i]+arr[i-1]):
        arr[i] = arr[i]+arr[i-1]

        
          
    
print(arr)
print(max(arr))