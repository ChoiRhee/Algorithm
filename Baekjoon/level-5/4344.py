c = int(input())

for i in range(c):
  all = list(map(int, input().split()))
  n = all[0]
  all.pop(0)
  avg = sum(all) / n
  cnt = 0
  for a in all:
    if a > avg:
      cnt += 1
  print('%.3f%%'%(cnt/n*100))
