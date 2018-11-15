class Solution(object):

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if len(matrix) == 0:
        	return 0

        heights = [0] * len(matrix[0])
        max_area = 0
        prev_lefts = [0]*len(matrix[0])
        prev_rights = [len(matrix[0])-1]*len(matrix[0])
        for row in matrix:
        	for col in range(len(matrix[0])):
        		elem = row[col]
        		if elem == '0':
        			heights[col] = 0
        		else:
        			heights[col] += 1

        	lefts = []
        	left = None
        	for col in range(len(matrix[0])):
        		if row[col] == '0':
        			left = None
        			lefts.append(0)
        		elif left is None:
        			left = col
        			lefts.append(max(left, prev_lefts[col]))
        		else:
        			lefts.append(max(left, prev_lefts[col]))
        		

        	rights = []
        	right = None
        	for col in range(len(matrix[0])-1,-1,-1):
        		if row[col] == '0':
        			right = None
        			rights.append(len(matrix[0])-1)
        		elif right is None:
        			right = col
        			rights.append(min(right, prev_rights[col]))
        		else:
        			rights.append(min(right, prev_rights[col]))
        	rights.reverse()

        	prev_lefts = lefts
        	prev_rights = rights

        	for i in range(len(heights)):
        		if row[i] == '1':
        			max_area = max(max_area, heights[i] * (rights[i] - lefts[i]+1))
        return max_area


if __name__ == '__main__':

	matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
	print Solution().maximalRectangle(matrix)


        