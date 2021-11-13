# https://programmers.co.kr/learn/courses/30/lessons/12934
def solution(n):
    for i in range(n+1):
        if i*i == n:
            return (i+1)*(i+1)
    return -1
