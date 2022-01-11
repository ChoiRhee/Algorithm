x, y, w, h = map(int, input().split())
# x, y 이미 지나온 거리 & w-x, h-y 더 갈 수 있는 거리
print(min(x, y, w-x, h-y))