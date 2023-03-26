from itertools import permutations
N = int(input())
valueStorage = list(map(int, input().split()))

operatorInput = list(map(int, input().split()))
operatorBox = ["+", "-", "*", "/"]
operatorStorage = []

result=[]
output=[]
#operatorStorage에 담기
for i in range(4):
    for j in range(operatorInput[i]):
        operatorStorage.append(operatorBox[i])

max_result = - int(1e9)
min_result = int(1e9)
#내부 값 구하기
# def findValue(a):
#     firstValue = valueStorage[0]
#     for i in range(N-1):
#         if(a[i]=="+"):
#             firstValue = firstValue + valueStorage[i+1]
#         elif(a[i]=="-"):
#             firstValue = firstValue - valueStorage[i+1]
#         elif(a[i]=="*"):
#             firstValue = firstValue * valueStorage[i+1]
#         else:
#             if(firstValue<0):
#                 firstValue = -(abs(firstValue)) // valueStorage[i+1]
#             else:
#                 firstValue = firstValue // valueStorage[i+1]
#     max_result = max(max_result, result)
#     min_result = min(min_result, result)

max_result = - int(1e9)
min_result = int(1e9)

for operatorList in permutations(operatorStorage,N-1):
    firstValue = valueStorage[0]
    for i in range(N-1):
        if(operatorList[i]=="+"):
            firstValue = firstValue + valueStorage[i+1]
        elif(operatorList[i]=="-"):
            firstValue = firstValue - valueStorage[i+1]
        elif(operatorList[i]=="*"):
            firstValue = firstValue * valueStorage[i+1]
        else:
            if(firstValue<0):
                firstValue = -(abs(firstValue)) // valueStorage[i+1]
            else:
                firstValue = firstValue // valueStorage[i+1]
    max_result = max(max_result, firstValue)
    min_result = min(min_result, firstValue)
    

#permutation 구현하기
# bools = [0 for _ in range(N-1)]
# def dfs():
#     if(len(result)==N-1):
#         currentValue=findValue()
#         output.append(currentValue)
#     for i in range(N-1):
#         if(not bools[i]):
           
#            bools[i] = 1
#            result.append(operatorStorage[i])
#            dfs()
#            result.pop()
#            bools[i] = 0
# dfs()
print(max_result)
print(min_result)