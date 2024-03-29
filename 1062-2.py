import sys
from itertools import combinations
input = sys.stdin.readline

def convert(x):
    return ord(x) - ord('a')

def convert_2(arr):
    result = 0
    for a in arr:
        result |= (1 << a)
    return result

n, k = map(int, input().split())
s = set([convert(a) for a in ['a', 'c', 'i', 'n', 't']])
base = 0
for i in s:
    base |= (1 << i)
arr = [set(map(convert, input().strip())) for _ in range(n)]
arr_2 = [convert_2(a) for a in arr]
candidates = set().union(*arr) - s
answer = 0
if k < 5:
    print(0)
else:
    if len(candidates) <= (k - 5):
        print(n)
    else:
        for c in combinations(candidates, k - 5):
            temp = base
            for i in c:
                temp |= (1 << i)
            answer = max(answer, sum(1 if (temp & a) == a else 0 for a in arr_2))
        print(answer)