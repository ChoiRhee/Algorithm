# https://programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    rev = []
    while n > 0:
        rev.append(n % 3)
        n = n // 3
    
    answer = 0
    for idx, i in enumerate(reversed(rev)):
        answer += i * (3**idx)
        
    return answer
