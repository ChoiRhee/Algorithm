# https://programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    up = ''
    low = ''
    for ss in s:
        if ss.isupper():
            up += ss
        else:
            low += ss
    return ''.join(sorted(low, reverse = True) + sorted(up, reverse = True))
