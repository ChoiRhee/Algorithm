# https://programmers.co.kr/learn/courses/30/lessons/12916
def s(s):
    s = s.lower()
    
    p = [s[i] == 'p' for i in range(len(s))]
    y = [s[i] == 'y' for i in range(len(s))]
    
    return sum(p) == sum(y)

def solution(s):
    return s.lower().count('y') == s.lower().count('p')
