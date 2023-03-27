
k = int(input())
klist = list(map(str, input().split()))

levelDown = range(9,-1,-1)

bools =[0 for _ in range(k)]
finalCheck=False
#Permutation from 0123 -> 987
# i == index, value
def check(array):
    for i in range(k):
        if (not((klist[i]==">" and array[i]>array[i+1]) or(klist[i]=="<" and array[i]<array[i+1]))):
            return False
    return True
         

def findSmall():
    if(finalCheck):
        return
    
    if len(ansSmall)==k+1:
        if (check(ansSmall)):
            finalCheck = True
        return 
    else:
        for i in range(0,10):
            if not bools[i]:
                ansSmall.append(i)
                bools[i] =1
                findSmall()
                if(finalCheck):
                    return
                bools[i] =0
                ansSmall.pop()

def findBig():
    if(finalCheck):
        return
    
    if len(ansBig)==k+1:
        if (check(ansBig)):
            finalCheck = True
        return 
    else:
        for i in range(9,-1,-1):
            if not bools[i]:
                ansBig.append(i)
                bools[i] =1
                findSmall()
                if(finalCheck):
                    return
                bools[i] =0
                ansBig.pop()
                
ansSmall=[]
ansBig=[]
findSmall()
bools =[0 for _ in range(k)]
finalCheck=False
findBig()

print(ansBig)
print(ansSmall)
