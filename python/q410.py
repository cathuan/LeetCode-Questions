class Solution(object):

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
    
        i = 0
        j = sum(nums)
        mid = (i+j)/2

        # binary search i, j such that self.hasMaxArray(i) = False and self.hasMaxArray(j) = True
        # The answer should be j.
        while j - i > 1:
            if self.hasMaxArray(nums, m, mid):
                j = mid
            else:
                i = mid
            mid = (i+j)/2
        return j

    # return True if splitArray(nums, m) >= x
    def hasMaxArray(self, nums, m, x):

        count = m
        partialSum = 0
        for num in nums:
            if count > 1:
                if partialSum + num <= x:
                    partialSum += num
                else:
                    count -= 1
                    # Here it's an edge case.
                    # If we don't check and return here, num might be put in partialSum > x silently.
                    if num > x:
                        return False
                    partialSum = num
            else:
                partialSum += num
        return partialSum <= x


if __name__ == "__main__":

    print Solution().splitArray([2,3,1,2,4,3], 5)