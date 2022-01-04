# N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
# 3, 5 봉지
N = int(input())
cnt = N
tmp = 0

if N%5 == 0:
    cnt = N//5
elif N == 3:
    cnt = 1
else:
    for i in range(1, N//5+1):
        if (N-5*i)%3 == 0:
            tmp = i + (N-5*i)//3
        elif N%3 == 0:
            tmp = N//3
        
        if tmp != 0 and cnt > tmp:
            cnt = tmp
    if tmp == 0:
        cnt = -1

print(cnt)