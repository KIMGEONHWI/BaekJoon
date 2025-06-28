nums = list(map(int, input().split()))
order = input().strip()

nums.sort()

mapping = {'A': nums[0], 'B': nums[1], 'C': nums[2]}

print(' '.join(str(mapping[ch]) for ch in order))
