# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    lost.sort(); reserve.sort()

    answer = n
    
    for lo in lost: # 잃어버렸는데 여분도 있는 경우
        if lo in reserve:
            lost.remove(lo)
            reserve.remove(lo)
            
    for lo in lost: # 잃어버리고 여분 없는 경우
        if lo in reserve:
            reserve.remove(lo)
        elif lo-1 in reserve:
            reserve.remove(lo-1)
        elif lo+1 in reserve:
            reserve.remove(lo+1)
        else:
            answer -= 1

    return answer
