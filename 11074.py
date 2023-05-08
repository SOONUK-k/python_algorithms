
# 수빈이의 현재 채널 100
N = int(input())                        # 이동하려는 채널
M = int(input())                        # 고장난 버튼의 개수
select_num = []
ans = abs(N - 100)
if M > 0:
    no = list(map(int, input().split()))    # 안 눌리는 버튼의 개수
else:
    print(min(ans, len(str(N))))
    exit(0)



def recur(cur, cnt):
    global ans
    if M == 0:
        print(len(str(N)))
        exit(0)
    if cur == 6:		
        if cnt > 0:						# cnt는 선택! 하나도 선택한게 없으면 x
            total_join = "".join(select_num)
            less = len(total_join)
            ans = min(ans, abs(int(total_join) - N)+less)
        return
    for button in range(0,10):
        if button in no:
            continue
        select_num.append(str(button))
        recur(cur + 1, cnt + 1)
        select_num.pop()
        recur(cur + 1, cnt)

recur(0, 0)
print(ans)