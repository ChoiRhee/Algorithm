# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    answer = []
    not_clear = {x:0 for x in range(1, N+1)}
    
    for i in range(1, N+1):
        fail = 0
        got = 0
        
        for j in range(len(stages)):
            if stages[j] == i:
                fail += 1
            if stages[j] >= i:
                got += 1
        
        not_clear[i] =  fail/got

    not_clear = sorted(not_clear.items(), key = lambda x: x[1], reverse=True)
    
    for n in not_clear:
        answer.append(n[0])
        
    return answer
