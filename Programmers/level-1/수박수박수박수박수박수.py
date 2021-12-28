# https://programmers.co.kr/learn/courses/30/lessons/12922
def s(n):
    answer = ''
    for i in range(1, n+1):
        if i % 2 != 0:
            answer += '수'
        else:
            answer += '박'
    return answer

def solution(n):
    return '수박' * (n//2) + '수' * (n%2)