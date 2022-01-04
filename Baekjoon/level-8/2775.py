# “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”
# k층 n호
T = int(input())
for t in range(T):
    K = int(input())
    N = int(input())
    home = [[x+1 for x in range(N)]]
    for k in range(1, K+1):
      new_floor = []
      tmp = 0
      for n in range(N):
        tmp += home[k-1][n]
        new_floor.append(tmp)
      home.append(new_floor)
    print(home[K][N-1])