N, X = map(int, input().split())
A = list(input().split())
out = []
for n in range(N):
  if int(A[n]) < X:
    out.append(A[n])
print(' '.join(out))