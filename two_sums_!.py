
nums = [3,5,6,8,5]

target = 6

n = len(nums)
def sum(target):
	for i in range(0,n):
		for j in range(i+1, n):
			sum = nums[i]+ nums[j]
			if(sum == target):
				print(" value at indices ", i ,"+",j, " = ", target)
	if(sum!= target):
		print("not found")
sum(6)
		