# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    a = arr[0]
    answer = [a]
    
    for i in range(1, len(arr)):
        if a != arr[i]:
            answer.append(arr[i])
            a = arr[i]
            
    return answer
