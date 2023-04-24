from typing import List, Tuple

def check(array, k, inequalities):
    for i in range(k):
        if not ((inequalities[i] == ">" and array[i] > array[i+1]) or (inequalities[i] == "<" and array[i] < array[i+1])):
            return False
    return True

def findSmall(ansSmall, bools, k, inequalities):
    if len(ansSmall) == k+1:
        if check(ansSmall, k, inequalities):
            return ansSmall
        return None
    else:
        for i in range(0, 10):
            if not bools[i]:
                ansSmall.append(i)
                bools[i] = 1
                result = findSmall(ansSmall, bools, k, inequalities)
                if result is not None:
                    return result
                bools[i] = 0
                ansSmall.pop()
    return None

def findBig(ansBig, bools, k, inequalities):
    if len(ansBig) == k+1:
        if check(ansBig, k, inequalities):
            return ansBig
        return None
    else:
        for i in range(9, -1, -1):
            if not bools[i]:
                ansBig.append(i)
                bools[i] = 1
                result = findBig(ansBig, bools, k, inequalities)
                if result is not None:
                    return result
                bools[i] = 0
                ansBig.pop()
    return None

def max_min_integer(k: int, inequalities: List[str]) -> Tuple[str, str]:
    ansSmall = []
    ansBig = []

    bools_small = [0 for _ in range(10)]
    ansSmall = findSmall(ansSmall, bools_small, k, inequalities)
    
    bools_big = [0 for _ in range(10)]
    ansBig = findBig(ansBig, bools_big, k, inequalities)

    return ''.join(map(str, ansBig)), ''.join(map(str, ansSmall))

# Example usage
k = 2
inequalities = ['<', '>']
print(max_min_integer(k, inequalities))  # Output: ('897', '021')
