import sys

sys.setrecursionlimit(10**5)

n,k = map(int, input().split())

if k<5:
    print(0)
    quit()

must =0
for alpha in 'antic':
    order = ord(alpha) -ord('a')
    must = must | (1<<order)


words =[]
for _ in range(n):
    word = input()
    b = 0
    for alpha in word:
        #takes each letter as a number
        order = ord(alpha) - ord('a')
        b = b| 1<<order
    #b <- becomes a bitmasked number of each word
    words.append(b)

def check(learn):
    read = 0
    for j in range(n):
        word = words[j]
        if(learn & word) ==word:
            read +=1
    return read

def recursion(idx, learn):
    global answer
    if idx >26:
        return

    if bin(learn).count('1') ==k:
        answer = max(answer, check(learn))
        return
    
    if must & (1<<idx):
        recursion(idx +1, learn |(1<<idx))
    else:
        recursion(idx +1, learn)
        recursion(idx +1, learn |(1<<idx))

answer = 0
recursion(0,0)
print(answer)
