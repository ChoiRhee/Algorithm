n = int(input())

for i in range(n):
    cnt, st = input().split()
    cnt = int(cnt)
    new = ''
    for j in range(len(st)):
       new += st[j] * cnt
    print(new)