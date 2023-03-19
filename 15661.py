import sys; input = sys.stdin.readline
from itertools import combinations
N = int(input())
grid = [list(map(int, input().split()))for _ in range(N)]
ans=[]
result = []
#ans: 뽑은 index보관, result: 최종값 출력을 위한 값 저장

def countScore():
    


    return 10

def dfs(nu, startIndex):
    if len(ans) ==nu:
        #점수합산 logic
        result.append() #점수차 
    for i in range(startIndex,N):
        ans.append(i)
        dfs(nu, i+1)
        ans.pop()



#Main Logic
for nu in range(1, N//2):
    dfs(nu,0)
print(min(result))
