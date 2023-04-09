
from itertools import product

def findNumList():
    result =[]
    for i in range(len(blankPosition)):
        fullBag = range(10)
        outBag =[]
        cnt=0
        #가로줄 제거
        for j in range(9):
            if(sdoqu[blankPosition[i][0]][j] != 0):
                fullBag[sdoqu[blankPosition[i][0]][j]] = 0
        #세로줄 제거
        for j in range(9):
            if(sdoqu[j][blankPosition[i][1]] != 0):
                fullBag[sdoqu[j][blankPosition[i][1]]] = 0
        #3X3제거
        standardY = blankPosition[i][0]//3
        standardX = blankPosition[i][1]//3
        for j in range(3):
            for k in range(3):
                if(sdoqu[(3*standardY)+j][(3*standardX)+k] != 0):
                    fullBag[sdoqu[(3*standardY)+j][(3*standardX)+k]] = 0
        #남은 수 꺼내기
        for j in range(10):
            if(fullBag[j] != 0):
                cnt+=1
                outBag.append(fullBag[j])
        #최종담기
        result.append((outBag,cnt))
    return result
    



def findSdoqu():
    #find possible numList
    possibleNumList = findNumList(blankPosition)

    #크기 추출 후 -> 배열 변환
    lengthNumList = len(possibleNumList)
    dimensions = [ possibleNumList[i][1] for i in range(lengthNumList)]
    ranges = [range(dim) for dim in dimensions]

    #곱연산 하여 한개 경우씩 판별하기
    for i in product(*ranges):
        #스도쿠에 값 집어넣기 
        iIndex=0
        for j in range(len(blankPosition)):     
            sdoqu[blankPosition[j][0]][blankPosition[j][1]] = possibleNumList[iIndex][0][i[iIndex]]
            iIndex+=1
        # 유효한 스도쿠인지 확인

        #















if __name__ == "__main__":

    blankPosition =[]
    sdoqu =[]
    for i in range(9):
        eachRange = list(map(int, input().split()))
        sdoqu.append(eachRange)

        #find blank position
        for j in range(9):
            if(eachRange[j]==0):
                ## i==y, j ==x
                blankPosition.append((i,j))

    output=findSdoqu()     
    print(output)      

