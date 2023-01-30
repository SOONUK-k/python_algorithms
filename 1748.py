N = int(input())
str = str(N)
strLen = len(str)
count = 0
count += (N-pow(10,strLen-1)+1)*strLen
for i in range(1,strLen):
    count += (9*pow(10,i-1)*i)
print(count)