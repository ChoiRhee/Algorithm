# https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3
from itertools import combinations
def solution(nums):
    answer = [sum(k) for k in combinations(nums, 3)]

    prime_cnt = 0
    for i in range(len(answer)):
        for j in range(2, answer[i]):
            if answer[i] % j == 0: break
        if j == answer[i] - 1: prime_cnt += 1

    return prime_cnt
