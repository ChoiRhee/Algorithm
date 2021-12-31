# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
n = int(input())
for i in range(n):
  a, b = map(int, input().split())
  print('Case #%d: %d + %d = %d'%(i+1, a, b, a+b))