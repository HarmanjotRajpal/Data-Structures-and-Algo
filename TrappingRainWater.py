class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxL=0
        maxR=0
        # two pointer for while loop left at start of loop and right at end of loop
        left = 0
        right = len(height)-1
        water = 0
        
        while left < right:
        
            #checking if value at left is < right
            if height[left] < height[right]:
            
                # updating maxL 
                if height[left] >= maxL:
                    maxL = height[left]
                    left = left+1
                else:
                    #updating water 
                    water = water +(maxL - height[left])
                    left = left + 1
            else:
                #updating maxR
                if height[right]>= maxR:
                    maxR = height[right]
                    right= right -1
                else:
                    #updating water
                    water = water + (maxR - height[right])
                    right = right-1
        return water
            
