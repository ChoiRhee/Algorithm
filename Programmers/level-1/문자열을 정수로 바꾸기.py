# https://programmers.co.kr/learn/courses/30/lessons/12925
def solution(s):
    try:
        return int(s)
    except:
        if s[0] == '+':
            return int(s[1:])
        else:
            return -1 * int(s[1:])
