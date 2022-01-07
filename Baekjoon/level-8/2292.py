N = int(input())
n = 1
cnt = 1
while N > n:
    n += 6*cnt
    cnt += 1
print(cnt)