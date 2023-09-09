while True :
    nums =list(map(int, input().split()))
    max_n=max(nums)
    if sum(nums) == 0:
        break
    nums.remove(max_n)
    if nums[0]**2+nums[1]**2==max_n**2:
        print("right")
    else:
        print("wrong")
