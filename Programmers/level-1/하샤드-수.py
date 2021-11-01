# https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3
def s(x):
    if x in [1, 10, 100, 1000, 10000] or x < 10:
        return True
    elif x < 100:
        if x % ((x - x//10*10) + x//10) == 0:
            return True
    elif x < 1000:
        if x % ((x - x//10*10) + (x//10 - x//100*10) + x//100) == 0:
            return True
    elif x < 10000:
        if x % ((x - x//10*10) + (x//10 - x//100 * 10) + (x//100 - x//1000*10) + x//1000) == 0:
            return True
    return False

def ss(x):
    y = str(x); sum = 0
    for i in range(len(y)):
        sum += int(y[i])
    if x % sum == 0:
        return True
    return False

def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0
