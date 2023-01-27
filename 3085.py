

li=[0, 0, 0]
ans = list(map(int, input().split()))
cnt=0

while(li != ans):
    cnt+=1
    li[0] +=1
    li[1] +=1
    li[2] +=1
    if(li[0]==16):
        li[0]=1
    if(li[1]==29):
        li[1]=1
    if(li[2]==20):
        li[2]=1  

print(cnt)