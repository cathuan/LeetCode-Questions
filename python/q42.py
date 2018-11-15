class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        heights = height
        trapped = 0
        stack = []
        for i in range(len(heights)):
        	height = heights[i]
        	while len(stack) > 0 and height > heights[stack[-1]]:
        		j = stack.pop()
        		if len(stack) == 0:
        			continue
        		added_area = (min(height, heights[stack[-1]]) - heights[j]) * (i-stack[-1]-1)
        		trapped += added_area
        	stack.append(i)
        return trapped


if __name__ == "__main__":

	print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])