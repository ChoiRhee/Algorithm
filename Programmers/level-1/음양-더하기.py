# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] == True else -1 * absolutes[i] for i in range(len(signs))])
