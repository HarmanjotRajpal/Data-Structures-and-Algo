#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """ 
        count = 0
        for i in range(0, len(nums)):
            if (nums[i] != 0):
                nums[count], nums[i] = nums[i], nums[count]
                count = count + 1
        return nums
