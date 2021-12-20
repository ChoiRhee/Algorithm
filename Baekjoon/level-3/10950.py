# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
num = int(input())
while num > 0:
    A, B = map(int, input().split())
    print(A+B)
    num -= 1
