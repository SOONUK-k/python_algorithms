N = int(input())
lis = [0] * (N+1)

li = list(map(int, input().split(" ")))

#들어온 요소 갯수
size= len(li)

#lis 안에값 있음
# 개당 가격 배열에 각 값을 집어넣기
for i in range(0, size):
    lis[i+1] = li[i]
    

# n개 살때 가장 비싼것을 배열에 집어넣기
for i in range(2, N+1):
    save =lis[i]
    for j in range (1, (i//2)+1 ):
        if((lis[j] + lis[i-j]) < save):
                save = lis[j] + lis[i-j]
    lis[i] = save

# 최종출력
print(lis[N])
