# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    
    for i, answer in enumerate(answers):
        if answer == a[i%len(a)]:
            score[0] += 1
        if answer == b[i%len(b)]:
            score[1] += 1
        if answer == c[i%len(c)]:
            score[2] += 1
    
    m = max(score)
    cor = [1, 2, 3]
    
    result = [cor[i] for i in range(3) if score[i] == m]

    return result
