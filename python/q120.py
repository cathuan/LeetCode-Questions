class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0: return 0
        
        final_result = self.localMinimalTotal(triangle)
        return min(final_result)

    def localMinimalTotal(self, triangle):
        if len(triangle) == 1:
            assert len(triangle) == 1
            v = triangle[0]
            return v
        
        pre_result = self.localMinimalTotal(triangle[:-1])
        final_result= []
        for i in range(len(triangle[-1])):
            val = triangle[-1][i]
            if i == 0:
                final_result.append(val + pre_result[i])
            elif i < len(triangle[-1])-1:
                final_result.append(min(pre_result[i-1],pre_result[i])+val)
            if i == len(triangle[-1])-1:
                final_result.append(pre_result[-1]+val)
        return final_result
                

if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3],[5,6,5,7,6],[7,5,2,9,11]]
    n = Solution().minimumTotal(triangle)
    print(n)