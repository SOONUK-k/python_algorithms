import sys
T = int(sys.stdin.readline())

def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

for _ in range (T):    
    M, N, x, y = map(int, sys.stdin.readline().split())
    gcdNum =gcd(M,N)
    yMove= x
    find = False
    while(yMove<=M*N/gcdNum+x):
        if(yMove%N == y%N):
            print(yMove)
            find = True
            break
        yMove +=M

    if(not find):
        print(-1)
