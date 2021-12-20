# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
num = int(input())
nums = list(map(int, input().split()))

print(min(nums), max(nums))
