# 홀수번째 대각선: 분자는 n~1, 분모는 1~n
# 짝수번째 대각선: 분자 1~n, 분모 n~1
n = int(input())
num = 0 # 몇 번째 줄인지
cnt = 0 # 칸 개수

while cnt < n:
    num += 1
    cnt += num
cnt -= num # while 마지막에 더해지니까

if num % 2 == 0: # 짝수번째 대각선: 분자1~n, 분모 n~1
    up = n - cnt
    down = num - up + 1

else: # 홀수번째 대각선: 분자 n~1, 분모 1~n
    down = n - cnt
    up = num - down + 1

print(f"{up}/{down}")