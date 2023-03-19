import sys; input = sys.stdin.readline
from itertools import combinations

N = int(input())
grid=  [list(map(int, input().split())) for _ in range(N)]


member = range(0,N) #index == value
result =[]

def scoreCounter(arr):
    if len(arr)==1:
        return 0
    
    score = 0
    for i in combinations(arr,2):
        person1 = i[0]
        person2 = i[1]
        score += grid[person1][person2]
        score += grid[person2][person1]
    return score

# s == list of Start member
# l == list of Link member

#Main logic start
#Goup start team
for memberCount in range(1, N//2+1):
    breakDecide = 0
    for s in combinations(member, memberCount):
        l=[]
        #Goup link team
        for i in member:
            if i not in s:
                l.append(i)

        sScore = scoreCounter(s)
        lScore = scoreCounter(l)
        willAppend = abs(sScore-lScore)
        if(willAppend==0):
            breakDecide=1
            result.append(willAppend)
            break

        result.append(willAppend)
    if(breakDecide):
        break
        
print(min(result))