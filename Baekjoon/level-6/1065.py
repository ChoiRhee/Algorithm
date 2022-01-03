'''어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. '''
N = int(input())
hansu = 0

for i in range(1, N+1):
  num_list = list(map(int, str(i))) # 각 자리 수를 넣기 위해 str로 바꿨다가 다시 int로 바꿔서 저장
  if i < 100:
    hansu += 1 # 1부터 99는 모두 한수
  elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
    hansu += 1 # 각 자리 수가 등차수열이면 함수

print(hansu)