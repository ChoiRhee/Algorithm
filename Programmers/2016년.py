# https://programmers.co.kr/learn/courses/30/lessons/12901
from datetime import date
def solution(a, b):
    name = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return name[date(2016, a, b).weekday()]
