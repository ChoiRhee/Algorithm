# 45분 일찍 알람 설정하기
H, M = map(int, input().split())

if H > 0 and M < 45:
    print(H-1, 15+M)
elif H == 0 and M < 45:
    print(23, 15+M)
else:
    print(H, M-45)
