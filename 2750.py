N = int(input().strip())
nums = [int(input().strip()) for _ in range(N)]
nums.sort()
for num in nums:
    print(num)
