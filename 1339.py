
N = int(input())
wordStore =[]
valueStore =[]
#
for _ in range(N):
    #입력받기
    eachWord = str(input())
    #단어길이
    #각 글자를 가져온다음에 없으면 집어넣고 값 더하기
    eachWordLength = len(eachWord)
    for i in range(eachWordLength):
        eachCharacter = eachWord[i]

        haveIndex=20
        #검증로직
        #1. hasSameword? -> then return the index
        for j in range(len(wordStore)):
            if(wordStore[j]==eachCharacter):
                haveIndex=j
        
        #2. 받은적이 없는 경우
        if(haveIndex == 20):
            wordStore.append(eachCharacter)
            valueStore.append(1*(10**(len(eachWord)-(i+1))))
        #. 받은적이 있고 index를 반환받음
        else:
            valueStore[haveIndex] += (1*(10**(len(eachWord)-(i+1))))

valueStore.sort(reverse=True)
sum = 0
sumValue = 9
for k in range(len(valueStore)):
    sum += sumValue*valueStore[k]
    sumValue-=1

print(sum)
