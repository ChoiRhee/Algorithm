# https://programmers.co.kr/learn/courses/30/lessons/1845
import pandas as pd
def solutio(nums):
    nums = pd.Series(nums)
    answer = len(nums.unique())
    if answer > len(nums)/2:
        return len(nums)/2
    
    return answer

def solution(nums):
    answer = len(set(nums))
    if answer > len(nums)/2:
        return len(nums)/2
    return answer
