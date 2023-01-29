size = list(map(int, input().split()))

N = size[0]
M = size[1]

numMatrix = []
ansMatrix = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    lineNum = list(map(int, input().split()))
    numMatrix.append(lineNum)

# i는 가로길이
# j는 세로길이
# numMatrix[j][i]

for j in range(N):
    for i in range(M):
        maxNum=0
        #청록색 도형
        if(i+3<M):
            num = numMatrix[j][i] + numMatrix[j][i+1] + numMatrix[j][i+2] + numMatrix[j][i+3]
            if(num>maxNum):
                maxNum = num
        #청록색 회전 도형
        if(j+3<N):
            num = numMatrix[j][i] + numMatrix[j+1][i] + numMatrix[j+2][i] + numMatrix[j+3][i]
            if(num>maxNum):
                maxNum = num        

        #노란색 도형
        if(i+1<M and j+1<N):
            num = numMatrix[j][i] + numMatrix[j][i+1] + numMatrix[j+1][i] + numMatrix[j+1][i+1]
            if(num>maxNum):
                maxNum = num
        
        #주황색 도형1
        if(i+1<M and j+2<N):
            num = numMatrix[j][i] + numMatrix[j+1][i] + numMatrix[j+2][i] + numMatrix[j+2][i+1]
            if(num>maxNum):
                maxNum = num

        #주황색 도형2
        if(i+1<M and j+2<N):
            num = numMatrix[j][i+1] + numMatrix[j+1][i+1] + numMatrix[j+2][i+1] + numMatrix[j+2][i]
            if(num>maxNum):
                maxNum = num
        #주황색 도형3
        if(i+1<M and j+2<N):
            num = numMatrix[j][i] + numMatrix[j][i+1] + numMatrix[j+1][i+1] + numMatrix[j+2][i+1]
            if(num>maxNum):
                maxNum = num
        #주황색 도형4
        if(i+1<M and j+2<N):
            num = numMatrix[j][i] + numMatrix[j][i+1] + numMatrix[j+1][i] + numMatrix[j+2][i]
            if(num>maxNum):
                maxNum = num
        #주황색 도형5
        if(i+2<M and j+1<N):
            num = numMatrix[j][i] + numMatrix[j+1][i] + numMatrix[j+1][i+1] + numMatrix[j+1][i+2]
            if(num>maxNum):
                maxNum = num
        #주황색 도형6
        if(i+2<M and j+1<N):
            num = numMatrix[j][i+2] + numMatrix[j+1][i] + numMatrix[j+1][i+1] + numMatrix[j+1][i+2]
            if(num>maxNum):
                maxNum = num
        #주황색 도형7
        if(i+2<M and j+1<N):
            num = numMatrix[j][i] + numMatrix[j][i+1] + numMatrix[j][i+2] + numMatrix[j+1][i+2]
            if(num>maxNum):
                maxNum = num
        #주황색 도형8
        if(i+2<M and j+1<N):
            num = numMatrix[j][i] + numMatrix[j][i+1] + numMatrix[j][i+2] + numMatrix[j+1][i]
            if(num>maxNum):
                maxNum = num


        #초록색 도형1
        if(i+1<M and j+2<N):
            num = numMatrix[j][i] + numMatrix[j+1][i] + numMatrix[j+1][i+1] + numMatrix[j+2][i+1]
            if(num>maxNum):
                maxNum = num
        #초록색 도형2
        if(i+1<M and j+2<N):
            num = numMatrix[j][i+1] + numMatrix[j+1][i] + numMatrix[j+1][i+1] + numMatrix[j+2][i]
            if(num>maxNum):
                maxNum = num

        #초록색 도형5
        if(i+2<M and j+1<N):
            num = numMatrix[j][i] + numMatrix[j][i+1] + numMatrix[j+1][i+1] + numMatrix[j+1][i+2]
            if(num>maxNum):
                maxNum = num
        #초록색 도형6
        if(i+2<M and j+1<N):
            num = numMatrix[j][i+1] + numMatrix[j][i+2] + numMatrix[j+1][i] + numMatrix[j+1][i+1]
            if(num>maxNum):
                maxNum = num
        #보라색 도형1
        if(i+2<M and j+1<N):
            num = numMatrix[j][i] + numMatrix[j][i+1] + numMatrix[j][i+2] + numMatrix[j+1][i+1]
            if(num>maxNum):
                maxNum = num
        #보라색 도형2
        if(i+1<M and j+2<N):
            num = numMatrix[j][i] + numMatrix[j+1][i] + numMatrix[j+1][i+1] + numMatrix[j+2][i]
            if(num>maxNum):
                maxNum = num
        #보라색 도형3
        if(i+1<M and j+2<N):
            num = numMatrix[j][i+1] + numMatrix[j+1][i] + numMatrix[j+1][i+1] + numMatrix[j+2][i+1]
            if(num>maxNum):
                maxNum = num
        #보라색 도형4
        if(i+2<M and j+1<N):
            num = numMatrix[j][i+1] + numMatrix[j+1][i] + numMatrix[j+1][i+1] + numMatrix[j+1][i+2]
            if(num>maxNum):
                maxNum = num

        
        ansMatrix[j][i] = maxNum
max=0
for j in range(N):
    for i in range(M):
        if(ansMatrix[j][i] > max):
            max = ansMatrix[j][i]
print(max)

