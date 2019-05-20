#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
res =[]
        
for i in nums:
  if i !=0:
    res.append(i)
        
for i in range(0, len(res)):
  nums[i] = res[i]
  
for i in range(len(res), len(nums)):
  nums[i] = 0
        
print(nums)
