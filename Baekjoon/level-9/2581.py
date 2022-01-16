'''M이상 N이하의 자연수 중 소수인 것의 합 
둘째 줄에 최솟값 출력 
없을 경우는 -1 출력'''
m = int(input())
n = int(input())
prime = []

for i in range(m, n+1): # m~n 사이에서
    no = 0
    if i > 1:
        for j in range(2, i): # 소수 찾기
            if i%j == 0:
                no += 1 # 나누어 떨어지면 소수 아님!
                break
        if no == 0:
            prime.append(i)

if prime:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)