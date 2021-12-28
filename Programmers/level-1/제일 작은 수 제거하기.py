# https://programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    arr.pop(arr.index(min(arr)))
    if len(arr) == 0: arr = [-1]
    return arr
