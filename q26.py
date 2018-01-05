class Solution(object):
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        current = None
        
        for num in nums:
            if current is None:
                count += 1
                current = num
            else:
                if num != current:
                    count += 1
                current = num
        
        return count


if __name__ == "__main__":

    solution = Solution()

    s = solution.removeDuplicates([1,2,3,3,3,4,4])
    print s
    
