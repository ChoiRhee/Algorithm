# . @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다
n = int(input())

for _ in range(n):
    lst = input().split()
    num = float(lst[0])
    for o in lst[1:]:
        if o == '@':
            num *= 3
        elif o == '%':
            num += 5
        elif o == '#':
            num -= 7
    print('%.2f'%num)