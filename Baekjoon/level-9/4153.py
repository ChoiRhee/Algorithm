while True:
  nums = list(map(int, input().split()))
  if sum(nums) == 0:
    break
  else:
    nums.sort()
    if nums[2]**2 == nums[0]**2 + nums[1]**2:
        print('right')
    else:
        print('wrong')