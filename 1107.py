#GG

N = int(input())
strN = str(N)
B = [True for _ in range(10)]

#각자리 숫자 만들기용 리스트 선언
numBean = [[0,0] for _ in range(len(strN))]

result =[]
#사용불가 숫자 받기
M = int(input())
Mwrong = list(map(int, input().split()))

#사용불가한 숫자를 false로 변환
for i in range(Mwrong):
    B[i] = False
#순수 이동만 하기
result[0] = abs(N - 100)

#각 숫자별 위치잡기
numLen = len(str(N))
for i in range(numLen):
    #n번째 위치의 숫자 가져오기 conunt ++;
    atNum=int(strN[i])
    atNumlist =findNum(atNum)


def findNum(num1, num2, bools, ans):
     
    
    if(bools[num1]):
        return ans[0]
    else:
        findNum
