# https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    if len(s) in [4, 6]:
        try:
            int(s)
            return True
        except:
            return False
    return False
