#!/usr/bin/python

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height) == 0:
            return 0
        
        if len(height) == 1:
            return 0
        
        leftIndex = 0
        rightIndex = len(height)-1
        maxArea = min(height[leftIndex], height[rightIndex]) * (rightIndex - leftIndex)
        
        while leftIndex < rightIndex - 1:
            if height[leftIndex] < height[rightIndex]:
                leftIndex += 1
            else:
                rightIndex -= 1
            area = min(height[leftIndex], height[rightIndex]) * (rightIndex - leftIndex)
            maxArea = max(maxArea, area)
            
        return maxArea
        
        
if __name__ == "__main__":
    
    height = [1,8,6,2,5,4,8,3,7]
    print Solution().maxArea(height)