# 이전에 k광년을 이동하면 k-1 , k 혹은 k+1 광년만 다시 이동가능
# 처음 작동시 1광년 이동 -> 그 다음 0, 1, 2광년 이동 가능
### x지점에서 y지점을 향해 최소한의 작동 횟수로 이동
### y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.
T = int(input())
for t in range(T):
    x, y = map(int, input().split())
    distance = y - x
    cnt = 0
    move = 1
    moved = 0

    while moved < distance:
        cnt += 1
        moved += move
        if cnt % 2 == 0:
            move += 1
    print(cnt)