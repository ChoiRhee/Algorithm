input()
nums = list(map(int, input().split()))
cnt = 0

for n in nums:
    x = 0
    if n > 1:
        for i in range(2, n):
            if n%i == 0:
                x += 1
        if x == 0:
            cnt += 1

print(cnt)