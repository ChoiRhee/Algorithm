# https://programmers.co.kr/learn/courses/30/lessons/70128
def solution(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])
