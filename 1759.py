import sys; input = sys.stdin.readline

#문제에서 주어진 input 받기
L,C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
#조건 확인을 위한 모음이있는 리스트 생성
vowelArr = ["a","e","i","o","u"]

#기본 설계방향
#모음이 있는 인덱스를 찾고 
#모음이 포함된 배열이면 출력을하고, 그렇지 않으면 출력을 하지 않는 방향으로 설계

#ans는 input을 담아서 출력할 리스트
ans=[]
def vowelCheck(array):   
    for i in array:
        if i in vowelArr:
            return True
    return False

def consonantsCheck(array):
    check=0
    for i in array:
        if i not in vowelArr:
            check+=1
            if(check>=2):
                return True
    return False

#dfs를 이용한 백트래킹을 구현했습니다.
# 'ans=[]' 안에 L개가 되기 전까지는 리스트에 담고,
# L개가 된 경우에는 '적어도 1개의 모음이 포함되어있는지' 경우를 체크하고 
# C값이 최소 3이기 때문에, 모음이 1
def dfs(index):
    if len(ans)==L:
        if(vowelCheck(ans) and consonantsCheck(ans)):
            print(''.join(map(str,ans)))         
        return
    for i in range(index,len(arr)):
        ans.append(arr[i])
        dfs(i+1)
        ans.pop()


##Logic start
dfs(0)
