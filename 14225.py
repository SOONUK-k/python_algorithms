from itertools import combinations

N = int(input())
S = list(map(int, input().split()))


output = [ i for i in range(1,10000001)]


for i in range(1,N+1):
    for j in combinations(S, i):
        if(sum(j) <=10000000):
            output[sum(j)-1] = 0

for k in output:
    if(k != 0):
        print(k)
        break


