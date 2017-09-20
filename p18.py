import operator
nums = [0,0,0,0,0,0,0,0]
target = 0
nums.sort()
print(nums)
res = []
oneRes = []

for a in range(len(nums)-3):
	if (nums[a] == nums[a-1]) & (a > 0):
		continue
	bp = None
	for b in range(a+1, len(nums)-2):
		if nums[b] == bp:
			continue
		bp = nums[b]
		l = b + 1
		r = len(nums) - 1
		while l < r:
			if (nums[a] + nums[b] + nums[l] + nums[r] < target):
				l += 1
			elif(nums[a] + nums[b] + nums[l] + nums[r] > target):
				r -= 1
			elif(nums[a] + nums[b] + nums[l] + nums[r] == target):
				oneRes = [nums[a], nums[b], nums[l], nums[r]]
				res.append(oneRes)
				l += 1
				while (l <= r) and (nums[l] == nums[l-1]):
					l += 1
				r -= 1
				while (l <= r) and (nums[r] == nums[r+1]):
					r -= 1

print(res)