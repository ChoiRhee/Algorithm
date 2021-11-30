# https://programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    answer = ''
    words = s.split(' ')
    
    for w in words:
        for i in range(len(w)):
            if i % 2 != 0:
                answer += w[i].lower()
            else:
                answer += w[i].upper()
        answer += ' '

    return answer[:-1]
