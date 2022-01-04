T = int(input())
for t in range(T):
  H, W, N = map(int, input().split())
  if N % H == 0:
    floor = H
    room = N // H
  else:
    floor = N % H
    room = N//H + 1
  print(str(floor*100 + room))