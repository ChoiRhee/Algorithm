h, m = map(int, input().split())
plus = int(input())

if m + plus >= 60:
    tmp = (m + plus) //60
    m = (m+plus) - tmp*60
    h += tmp
    if h >= 24:
        h -= 24
else:
    m += plus

print(h, m)