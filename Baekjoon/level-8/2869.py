# 높이 V미터 올라가는 A미터 미끄러지는 B미터
a, b, v = map(int, input().split())

v = v - a
if v % (a-b) == 0:
    print(v//(a-b)+1)
else:
    print(v//(a-b)+2)