a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
x = 0; y = 0

if a[0] == b[0]:
    x = c[0]
    if a[1] == c[1]:
        y = b[1]
    else:
        y = a[1]
elif a[0] == c[0]:
    x = b[0]
    if a[1] == b[1]:
        y = c[1]
    else:
        y = a[1]
elif c[0] == b[0]:
    x = a[0]
    if c[1] == a[1]:
        y = b[1]
    else:
        y = c[1]

print(x, y)