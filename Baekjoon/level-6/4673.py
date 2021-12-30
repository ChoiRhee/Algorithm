# 생성자가 없는 숫자
R = [i+1 for i in range(10000)]
new = []

for i in range(1, 10001):
  for j in str(i):
    i += int(j)
  new.append(i)

selfnum = sorted(set(R) - set(new))
for s in selfnum: print(s)