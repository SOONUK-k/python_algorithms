N  = int(input())


for _ in range(N):
    result=[]
    eachWord = str(input())
    check = 0
    for i in range(len(eachWord)):
        eachCharacter = eachWord[i]
        if(eachCharacter=="("):
            result.append(")")
        else:
            if(len(result)==0):
                check+=1
                break
            else:
                result.pop()
    if(check == 0):
        if(len(result) ==0):
            print("YES")
        else: 
            print("NO")
    else:
        print("NO")