# https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3
def s(n):
    n = str(n)
    answer = [int(n[-i]) for i in range(1, len(n)+1)]
    return answer

def solution(n):
    answer = [int(i) for i in str(n)[::-1]]
    
    return answer
