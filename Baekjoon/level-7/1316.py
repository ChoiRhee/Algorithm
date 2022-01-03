'''그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.'''
# 첫째 줄에 단어의 개수 N. 둘째 줄부터 N개의 줄에 단어, 알파벳 소문자로만, 중복x
N = int(input())
cnt = N

for n in range(N):
  word = input() # N번 입력 받음

  for i in range(len(word)-1): # i, i+1 비교하니까
    if word.find(word[i]) > word.find(word[i+1]): # 이게 만족하면 중복된 문자가 있다는 의미
      # find는 맨 처음 등장한 자리 인덱스 반환하는 거라서 뒤에 나온 문자 인덱스가 앞의 문자보다 작으면 중복됐다는 의미
      # 'aaabndae'에서 i가 5일때 find(d) = 5, find(a) = 0 이라서 중복이라고 판단. -> a가 앞에 나왔는데 또 나왔다는 의미
      cnt -= 1 # 그룹단어가 아니면 개수 차감
      break

print(cnt)