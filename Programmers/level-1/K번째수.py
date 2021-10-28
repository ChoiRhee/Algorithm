# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
def solution(array, commands):
    #return [sorted(array[commands[i][0]-1: commands[i][1]])[commands[i][2]-1] for i in range(len(commands))]
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]
